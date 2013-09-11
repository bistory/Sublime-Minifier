import sublime
import re
if sublime.version() < '3':
    import urllib
    import urllib2
    from basecall import BaseCall
else:
    import urllib.request
    import urllib.parse
    from Minifier.compilers.basecall import BaseCall

class GoogleClosureCall(BaseCall):

    def exec_request(self):
        ua = 'Sublime Text - Google Closure'
        query = {
            'js_code': self.original.encode('utf-8'),
            'compilation_level': self.level,
            'output_info': "compiled_code" }
        url = "http://closure-compiler.appspot.com/compile"
        
        if sublime.version() < '3':
            data = urllib.urlencode(query)
        
            req = urllib2.Request(url, data, headers = { 'User-Agent': ua })
            file = urllib2.urlopen(req, timeout=self.timeout)
        else:
            data = urllib.parse.urlencode(query)
            binary_data = data.encode('utf8')
        
            req = urllib.request.Request(url, binary_data, headers = { 'User-Agent': ua })
            file = urllib.request.urlopen(req, timeout=self.timeout)

        mini_content = file.read().strip()

        if len(mini_content) > 0:
            return re.sub("[\n]+", " ", mini_content) if self.rm_new_lines else mini_content
        else:
            return None