import sys

count = 0
for line in sys.stdin.readlines():
    count += 1

sys.stdout.write('read ' + str(count) + ' lines')
