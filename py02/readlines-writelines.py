input_file = open('file.txt', 'r')
lines = input_file.readlines()
input_file.close()

output_file = open('copy.txt', 'w')
output_file.writelines(lines)
output_file.close()
