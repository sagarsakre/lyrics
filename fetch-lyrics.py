#!/usr/bin/env python

import HTMLParser
import urllib
import json
import sys
import re

base = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&'
query = urllib.urlencode({'q' :  sys.argv[1]+" lyrics azlyrics"})
response = urllib.urlopen(base + query).read()
data = json.loads(response)
print
print 'Fetching from .....'
print
print data['responseData']['results'][0]['url']
urlText = []

#Define HTML Parser
class parseText(HTMLParser.HTMLParser):
        
    def handle_data(self, data):
        if data != '\n':
            urlText.append(data)
    

#Create instance of HTML parser
lParser = parseText()

#Feed HTML file into parser
lParser.feed(urllib.urlopen(data['responseData']['results'][0]['url']).read())
lParser.close()
print
print 'Enjoy the Lyrics of',urlText[156],'brought to you by Sagar Sakre ...'
print 
print
print '--------------------------------------------------------------------'
first_twelve = urlText[155:600]
for each_line in first_twelve:
    if "/Android|webOS|iPhone|iPod|iPad|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent" in each_line:
        break
    else:
        print each_line

print '--------------------------------NO_FEAR-------------------------------'
