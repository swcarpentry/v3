input_file = open('count_bytes.py', 'r')
content = input_file.read()
input_file.close()
print len(content), 'bytes in file'
