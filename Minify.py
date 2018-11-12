from os import path

import sublime
import sublime_plugin

if sublime.version() < '3':
    from compilers import GoogleClosureCall, UglifyCall, ReducisaurusCall, CssminifierCall
else:
    from Minifier.compilers import GoogleClosureCall, UglifyCall, ReducisaurusCall, CssminifierCall

class BaseMinifier(sublime_plugin.TextCommand):
    '''Base Minifier'''

    def __init__(self, view):
        self.view = view
        self.window = sublime.active_window()
        self.settings = sublime.load_settings('Minifier.sublime-settings')

    def run(self, edit):
        selections = self.get_selections()
        CompilerCall = self.get_minifier()

        if CompilerCall is None:
            sublime.error_message('Please focus on the file you wish to minify.')
        else:
            threads = []
            for sel in selections:
                selbody = self.view.substr(sel)
                thread = CompilerCall(
                            sel,
                            selbody,
                            timeout=self.settings.get('timeout', 5),
                            level=self.settings.get('optimization_level', 'WHITESPACE_ONLY'),
                            rm_new_lines=self.settings.get('remove_new_lines', False))

                threads.append(thread)
                thread.start()
            
            # Wait for threads
            for thread in threads:
                thread.join()

            selections.clear()
            self.handle_threads(edit, threads, selections, offset=0, i=0, dir=1)

    def get_selections(self):
        selections = self.view.sel()

        # check if the user has any actual selections
        has_selections = False
        for sel in selections:
            if sel.empty() == False:
                has_selections = True

        # if not, add the entire file as a selection
        if not has_selections:
            full_region = sublime.Region(0, self.view.size())
            selections.add(full_region)

        return selections

    def handle_threads(self, edit, threads, selections, offset = 0, i = 0, dir = 1):

        next_threads = []
        for thread in threads:
            if thread.is_alive():
                next_threads.append(thread)
                continue
            if thread.result == False:
                continue
            self.handle_result(edit, thread, selections, offset)
        threads = next_threads

        if len(threads):
            before = i % 8
            after = (7) - before

            dir = -1 if not after else dir
            dir = 1 if not before else dir

            i += dir

            self.view.set_status('minify', '[%s=%s]' % (' ' * before, ' ' * after))

            sublime.set_timeout(lambda: self.handle_threads(edit, threads, selections, offset, i, dir), 100)
            return

        self.view.erase_status('minify')
        sublime.status_message('Successfully minified')

    def handle_result(self, edit, thread, selections, offset):
        sel = thread.sel
        original = thread.original
        result = thread.result

        if thread.error is True:
            sublime.error_message(result)
            return
        elif result is None:
            sublime.error_message('There was an error minifying the file.')
            return

        return thread

    def get_minifier(self):
        current_file = self.view.file_name()

        if current_file is None:
            return None
        else:
            file_parts = path.splitext(current_file)

            if file_parts[1] == '.js':
                compiler = self.settings.get('compiler', 'google_closure')
                compilers = {
                    'google_closure': GoogleClosureCall,
                    'uglify_js': UglifyCall
                }

                return compilers[compiler] if compiler in compilers else compilers['google_closure']
            elif file_parts[1] == '.css':
                compiler = self.settings.get('css_compiler', 'cssminifier')
                compilers = {
                    'reducisaurus': ReducisaurusCall,
                    'cssminifier': CssminifierCall
                }
                return compilers[compiler] if compiler in compilers else compilers['cssminifier']

    def get_new_line(self):
        CR = chr(0x0D)
        LF = chr(0x0A)
        endtypes = {'u': LF, 'w': CR+LF, 'm': CR}
        return endtypes[self.view.line_endings()[0].lower()]

class MinifyAutoMagic(sublime_plugin.EventListener):
    def on_post_save(self, view): 
        self.settings = sublime.load_settings('Minifier.sublime-settings')  
        file_can_minify_list = [ 'css', 'js']
        if self.settings.get('auto_minify_on_save', False ) == True:
            if view.file_name().split('.').pop().lower() in file_can_minify_list:
                sublime.status_message(' Starting auto minify for ' + view.file_name() );
                view.run_command('minify_to_file');
                #sublime.message_dialog( " AutoMinifyAndSave " + view.file_name()  );

class Minify(BaseMinifier):

    def handle_result(self, edit, thread, selections, offset):
        result = super(Minify, self).handle_result(edit, thread, selections, offset)

        if thread.error is None:
            if sublime.version() < '3':
                editgroup = self.view.begin_edit('minify')

            sel = thread.sel
            result = thread.result
            if offset:
                sel = sublime.Region(thread.sel.begin() + offset, thread.sel.end() + offset)

            if sublime.version() < '3':
                self.view.replace(edit, sel, result)
            else:
                self.view.replace(edit, sel, result.decode("utf-8"))

            if sublime.version() < '3':
                self.view.end_edit(edit)

class MinifyToFile(BaseMinifier):

    def run(self, edit):

        self.selections_completed = 0
        self.output = ""
        self.total_selections = len(self.get_selections())

        super(MinifyToFile, self).run(edit)

    def save(self, name):
        destination_file = path.join(
            self.file_path,
            name
        )

        extension = destination_file.split(".")
        extension = extension[-1]
        if("."+extension != self.extension):
            destination_file = destination_file+self.extension

        if sublime.version() < '3':
            with open(destination_file, 'w+', 0) as min_file:
                min_file.write(self.output.strip())
        else:
            with open(destination_file, 'wb+', 0) as min_file:
                min_file.write(bytes(self.output.strip(),'utf-8'))

        print (self.settings.get('open_on_min', True))
        if (self.settings.get('open_on_min', True) == True):
            self.window.open_file(destination_file)

    def handle_result(self, edit, thread, selections, offset):
        self.selections_completed += 1

        super(MinifyToFile, self).handle_result(edit, thread, selections, offset)

        if thread.error is None:
            if sublime.version() < '3':
                self.output = self.output + self.get_new_line() + thread.result
            else:
                self.output = self.output + self.get_new_line() + thread.result.decode('utf-8')

            # test if all the selections have been minified. if so, write all the output to the new file
            if self.selections_completed is self.total_selections:
                current_file = self.view.file_name()

                file_parts = path.splitext(current_file)
                self.extension = file_parts[1]

                self.file_path = path.dirname(current_file)

                options = self.settings.get('minify_options', {
                    "ask_file_name" : False,
                    "default_name" : None,
                    "suffix" : ".min"
                })

                if (options['default_name'] is None):
                    file_name_list = current_file.split('/')
                    real_file_name = file_name_list[-1]
                    placeholder = real_file_name
                else:
                    placeholder = options['default_name']

                if (self.settings.has('min_file_suffix')):
                    self.min_file_suffix = self.settings.get('min_file_suffix', '')
                elif (('suffix' in options) and (options['suffix'] is not None)):
                    self.min_file_suffix = options['suffix']
                else:
                    self.min_file_suffix = ""
                
                tmp = placeholder.split(".")
                if ( 1 < len(tmp) ):
                    tmp = tmp[:-1]

                placeholder = "".join(tmp) + self.min_file_suffix+ self.extension

                if (options['ask_file_name'] == True):
                    self.window.show_input_panel("File Name", placeholder, self.save, None, None);
                else:
                    self.save(placeholder)
