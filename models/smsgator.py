import urllib
from openerp import exceptions
  
def smsgatorSMS(username, password, destination, sender, message):
    params = {'username': username, 'password': password, 'recipient':destination, 'sender': sender, 
        'message' : message}
    sent = urllib.urlopen('http://smsmobile24.com/components/com_spc/smsapi.php?'
        + urllib.urlencode(params))
    print 'this portion of the code ran'
    code = sent.read()
    print code, sent.code
    print 'this is the code', code
    if code != "-2906":
        print "inside if ", code
        raise exceptions.Warning('Document Sent But SMS Wasnt Sent to the Department to Alert them of new document. Contact Solution Provider to rectify this!')
    return (sent.read(), sent.code)


