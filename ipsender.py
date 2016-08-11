import os
import urllib2
import json

# read latest ip from file
ip1 = open('ip.txt', 'r').read()
#print ip1

# get current ip
response = urllib2.urlopen('https://api.ipify.org?format=json')
ip2 = json.load(response)
ip2 = ip2['ip']
#print ip2

# compare ip's and send email if ip has changed
if ip1 == ip2:
    1 == 1
    #print "they are the same"
else:
    f = open("ip.txt","w")
    f.write(str(ip2))
    f.close()
    #print "different"
    os.system("echo \" %s \" | mail -s \"mokkula\" artturi@saunalahti.fi" % ip2)
