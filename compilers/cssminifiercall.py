import urllib
import urllib2
import re
import httplib
from basecall import BaseCall

class CssminifierCall(BaseCall):

    def exec_request(self):
    
        data = urllib.urlencode({
            'input': self.original })

        ua = 'Sublime Text - cssminifier'
        req = urllib2.Request("http://cssminifier.com/raw", data, headers = { 'User-Agent': ua, 'Content-Type': 'application/x-www-form-urlencoded' })
        file = urllib2.urlopen(req, timeout=self.timeout)

        mini_content = file.read().strip()

        if len(mini_content) > 0:
            return re.sub("[\n]+", " ", mini_content) if self.rm_new_lines else mini_content
        else:
            return None
