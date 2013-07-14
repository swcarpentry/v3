import sys, struct

# store:start
def store(outf, format, values):
    '''Store a list of lists, each of which has the same structure.'''
    length = struct.pack('i', len(format))
    outf.write(length)
    outf.write(format)
    for v in values:
        temp = [format] + v
        binary = struct.pack(*temp)
        outf.write(binary)
# store:end

# retrieve:start
def retrieve(inf):
    '''Retrieve data from a self-describing file.'''
    data = inf.read(struct.calcsize('i'))
    format_length = struct.unpack('i', data)[0]
    format = inf.read(format_length)
    record_size = struct.calcsize(format)
    result = []
    while True:
        data = inf.read(record_size)
        if not data:
            break
        values = list(struct.unpack(format, data))
        result.append(values)
    return result
# retrieve:end

# test:start
from cStringIO import StringIO
tests = [
    ['i',  [[17]]],
    ['ii', [[17, 18]]],
    ['ii', [[17, 18], [19, 20], [21, 22]]],
    ['if', [[17, 18.0], [19, 20.0]]]
]
for (format, original) in tests:
    storage = StringIO()
    temp = store(storage, format, original)
    storage.seek(0)
    final = retrieve(storage)
    assert original == final
# test:end
