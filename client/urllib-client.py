import urllib

instream = urllib.urlopen("http://www.third-bit.com/greeting.html")
lines = instream.readlines()
instream.close()
for line in lines:
    print line,
