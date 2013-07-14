import sys, os

print 'initial working directory:', os.getcwd()
os.chdir(sys.argv[1])
print 'moved to:', os.getcwd()
print 'contents:', os.listdir(os.curdir)
