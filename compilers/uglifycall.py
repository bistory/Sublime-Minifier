import urllib
import urllib2
from basecall import BaseCall

class UglifyCall(BaseCall):

    def exec_request(self):

        data = urllib.urlencode({
            'js_code': self.original.encode('utf-8'),
            'compilation_level': self.level,
            'output_info': "compiled_code" })

        ua = 'Sublime Text - Uglify'
        req = urllib2.Request("http://marijnhaverbeke.nl/uglifyjs", data, headers = { 'User-Agent': ua })
        try:
            file = urllib2.urlopen(req, timeout=self.timeout)
        except Exception:
            return None

        mini_content = file.read().strip()

        if len(mini_content) > 0:
            return re.sub("[\n]+", " ", mini_content) if self.rm_new_lines else mini_content
        else:
            return None