import urllib
import urllib2
import re
from basecall import BaseCall

class ReducisaurusCall(BaseCall):

    def exec_request(self):

        data = urllib.urlencode({
            'file': self.original })

        ua = 'Sublime Text - Reducisaurus'
        req = urllib2.Request("http://reducisaurus.appspot.com/css", data, headers = { 'User-Agent': ua, 'Content-Type': 'application/x-www-form-urlencoded' })
        file = urllib2.urlopen(req, timeout=self.timeout)

        mini_content = file.read().strip()

        if len(mini_content) > 0:
            return re.sub("[\n]+", " ", mini_content) if self.rm_new_lines else mini_content
        else:
            return None