import struct

packed = struct.pack('4c', 'a', 'b', 'c', 'd')
print 'packed string:', repr(packed)

left16, right16 = struct.unpack('hh', packed)
print 'as two 16-bit integers:', left16, right16

all32 = struct.unpack('i', packed)
print 'as a single 32-bit integer', all32[0]

float32 = struct.unpack('f', packed)
print 'as a 32-bit float', float32[0]
