import sys
print sys.platform
for mode in ('r', 'rb'):
    f = open('open_binary.py', mode)
    s = f.read(40)
    f.close()
    print repr(s)
