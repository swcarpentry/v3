import os

print 'does /home/swc exist?', os.path.exists('/home/swc')
print 'is it a directory?', os.path.isdir('/home/swc')
print 'what is its configuration directory?', os.path.join('/home/swc', 'conf')
print 'where is the configuration file?', os.path.split('/home/swc/conf/current.conf')
