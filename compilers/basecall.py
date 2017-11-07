import sublime
import sublime_plugin
import threading
if sublime.version() < '3':
    import urllib2
else:
    import urllib.error

class BaseCall(threading.Thread):

    def __init__(self, sel, string, timeout, level, rm_new_lines):
        self.sel = sel
        self.original = string
        self.timeout = timeout
        self.result = None
        self.level = level
        self.error = None
        self.rm_new_lines = rm_new_lines
        threading.Thread.__init__(self)

    def exec_request(self):
        return

    def run(self):
        if sublime.version() < '3':
            try:
                self.result = self.exec_request()
            except urllib2.HTTPError as e:
                self.error = True
                self.result = 'Minifier Error: HTTP error %s contacting API' % (str(e.code))
            except urllib2.URLError as e:
                self.error = True
                self.result = 'Minifier Error: ' + str(e.reason)
            except UnicodeEncodeError:
                self.error = True
                self.result = 'You can only use ASCII characters'
        else:
            try:
                self.result = self.exec_request()
            except urllib.error.HTTPError as e:
                self.error = True
                self.result = 'Minifier Error: HTTP error %s contacting API' % (str(e.code))
            except urllib.error.URLError as e:
                self.error = True
                self.result = 'Minifier Error: ' + str(e.reason)
            except UnicodeEncodeError:
                self.error = True
                self.result = 'You can only use ASCII characters'