#!/usr/bin/env python

import sys, os, Cookie
import cgitb; cgitb.enable()

# body:start
# Get old count.
count = 0
if os.environ.has_key('HTTP_COOKIE'):
    cookie = Cookie.SimpleCookie()
    cookie.load(os.environ['HTTP_COOKIE'])
    if cookie.has_key('count'):
        count = int(cookie['count'].value)

# Create new count.
count += 1
cookie = Cookie.SimpleCookie()
cookie['count'] = count

# Display.
print 'Content-Type: text/html'
print cookie
print
print '<html><body>'
print '<p>Visits: %d</p>' % count
print '</body></html>'
# body:end
