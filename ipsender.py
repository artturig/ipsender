import os
import urllib2
import json

response = urllib2.urlopen('https://api.ipify.org?format=json')
data = json.load(response)   
print data

os.system("echo \" %s \" | mail -s \"mokkula\" CHANGEME@email.fi" % data)
