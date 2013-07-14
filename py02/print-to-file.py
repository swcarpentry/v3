input_file = open('file.txt', 'r')
output_file = open('copy.txt', 'w')
for line in input_file:
    line = line.rstrip()
    print >> output_file, line
input_file.close()
output_file.close()
