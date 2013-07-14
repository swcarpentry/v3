#!/usr/bin/env python

import sys, cgi
import cgitb; cgitb.enable()

# body:start
# Get existing messages.
infile = open('messages.txt', 'r')
lines = [x.rstrip() for x in infile.readlines()]
infile.close()

# Add more data?
form = cgi.FieldStorage()
if form.has_key('newmessage'):
    lines.append(form.getfirst('newmessage'))
    outfile = open('messages.txt', 'w')
    for line in lines:
        print >> outfile, line
    outfile.close()
# body:end

# display:start
# Display.
print 'Content-Type: text/html'
print
print '<html><body>'
for line in lines:
    print '<p>' + line + '</p>'
print '''
<form action="http://www.third-bit.com/swc/message_form.py" method="post">
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
# display:end
