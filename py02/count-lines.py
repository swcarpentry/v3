input_file = open('count_lines.py', 'r')
count = 0
for line in input_file:
    count += 1
input_file.close()
print count, 'lines in file'
