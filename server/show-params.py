#!/usr/bin/env python
import cgi

print 'Content-type: text/html'
print
print '<html><body>'
form = cgi.FieldStorage()
for key in form.keys():
    value = form.getvalue(key)
    if isinstance(value, list):
        value = '[' + ', '.join(value) + ']'
    print '<p>%s: %s</p>' % (cgi.escape(key), cgi.escape(value))
print '</body></html>'
