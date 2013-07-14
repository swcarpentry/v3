input_file = open('file.txt', 'r')
output_file = open('copy.txt', 'w')
line = input_file.readline()
while line:
    output_file.write(line)
    line = input_file.readline()
input_file.close()
output_file.close()
