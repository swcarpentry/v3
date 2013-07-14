import struct

fmt = 'hh' # two 16-bit integers
x = 31
y = 65
binary = struct.pack(fmt, x, y)
print 'binary representation:', repr(binary)
normal = struct.unpack(fmt, binary)
print 'back to normal:', normal
