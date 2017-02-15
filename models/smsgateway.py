#!/usr/bin/env python
import urllib
  
def sendSMS(uname, pword, numbers, sender, message):
    params = {'uname': uname, 'pword': pword, 'selectednums': numbers, 
        'message' : message, 'from': sender}
    f = urllib.urlopen('https://www.txtlocal.co.uk/sendsmspost.php?'
        + urllib.urlencode(params))
    print 'this portion of the code ran'
    return (f.read(), f.code)
