import sys
import os

for filename in sys.argv[1:]:
    status = os.stat(filename)
    print filename, status.st_size, status.st_atime
