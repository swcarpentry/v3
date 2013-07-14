import struct

# pack:start
def pack_strings(strings):
    result = ''
    for s in strings:
        length = len(s)
        format = 'i%ds' % length
        result += struct.pack(format, length, s)
    return result
# pack:end

# unpack:start
def unpack_strings(buf):
    int_size = struct.calcsize('i')
    pos = 0
    result = []
    while pos < len(buf):
        length = struct.unpack('i', buf[pos:pos+int_size])[0]
        pos += int_size
        format = '%ds' % length
        s = struct.unpack(format, buf[pos:pos+length])[0]
        pos += length
        result.append(s)
    return result
# unpack:end

# test:start
if __name__ == '__main__':
    tests = ['', 'a', 'bcd']
    for i in range(len(tests)):
        t = tests[0:i+1]
        buffer = pack_strings(t)
        result = unpack_strings(buffer)
        assert result == t
# test:end
