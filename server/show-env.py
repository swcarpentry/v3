#!/usr/bin/env python

import os, cgi

# Headers and an extra blank line
print 'Content-type: text/html'
print

# Body
print '<html><body>'
keys = os.environ.keys()
keys.sort()
for k in keys:
    print '<p>%s: %s</p>' % (cgi.escape(k), cgi.escape(os.environ[k]))
print '</body></html>'
