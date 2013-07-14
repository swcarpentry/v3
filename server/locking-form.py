#!/usr/bin/env python

import sys, cgi, fcntl
import cgitb; cgitb.enable()

# body:start
# Get existing messages.
msgfile = open('messages.txt', 'r+')
fcntl.flock(msgfile.fileno(), fcntl.LOCK_EX)
lines = [x.rstrip() for x in msgfile.readlines()]

# Add more data?
form = cgi.FieldStorage()
if form.has_key('newmessage'):
    lines.append(form.getfirst('newmessage'))
    msgfile.seek(0)
    for line in lines:
        print >> msgfile, line

# Unlock and close.
fcntl.flock(msgfile.fileno(), fcntl.LOCK_UN)
msgfile.close()
# body:end

# Display.
print 'Content-Type: text/html'
print
print '<html><body>'
for line in lines:
    print '<p>' + line + '</p>'
print '''
<form action="http://www.third-bit.com/swc/locking_form.py" method="post">
  <p>Your message:
     <input name="newmessage" type="text"/>
  </p>
  <p>
    <input type="submit"/>
    <input type="reset"/>
  </p>
</form>
'''
print '</body></html>'
