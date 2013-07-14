import struct

# pack:start
def pack_vec(vec):
    buf = struct.pack('i', len(vec))
    for v in vec:
        buf += struct.pack('i', v)
    return buf
# pack:end

# unpack:start
def unpack_vec(buf):

    # Get the count of the number of elements in the vector.
    int_size = struct.calcsize('i')
    count = struct.unpack('i', buf[0:int_size])[0]

    # Get 'count' values, one by one.
    pos = int_size
    result = []
    for i in range(count):
        v = struct.unpack('i', buf[pos:pos+int_size])
        result.append(v[0])
        pos += int_size

    return result
# unpack:end

# test:start
if __name__ == '__main__':

    tests = [
        [],
        [1],
        [1, 2],
        [-3, 456, 7890]
    ]

    for t in tests:
        s = pack_vec(t)
        v = unpack_vec(s)
        assert v == t
# test:end
