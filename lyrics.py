#!/usr/bin/env python

import HTMLParser
import urllib
import json
import sys
import re

base = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&'
query = urllib.urlencode({'q' :  sys.argv[1]+"azlyrics"})
response = urllib.urlopen(base + query).read()
data = json.loads(response)
print
print 'Trying to get data from'
print data['responseData']['results'][0]['url']
print
print 'Enjoy the Lyrics of',sys.argv[1],'brought to you by Sagar Sakre'
urlText = []

#Define HTML Parser
class parseText(HTMLParser.HTMLParser):
        
    def handle_data(self, data):
        if data != '\n':
            urlText.append(data)
    

#Create instance of HTML parser
lParser = parseText()

#thisurl = data['responseData']['results'][0]['url']
#Feed HTML file into parser
lParser.feed(urllib.urlopen(data['responseData']['results'][0]['url']).read())
lParser.close()
#f1=open('./testfile', 'w+')
#for item in urlText:
#    f1.write(item)
#    print item
first_twelve = urlText[51:600]
for each_line in first_twelve:
    if "/Android|webOS|iPhone|iPod|iPad|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent" in each_line:
        break
    else:
        print each_line
#if prog.match(each_line):
