#            hex     binary
MERCURY    = 0x01  # 0001
PHOSPHORUS = 0x02  # 0010
CHLORINE   = 0x04  # 0100

# Sample contains mercury and chlorine
sample = MERCURY | CHLORINE
print 'sample: %04x' % sample

# Check for various elements
for (flag, name) in [[MERCURY,    "mercury"],
                     [PHOSPHORUS, "phosphorus"],
                     [CHLORINE,   "chlorine"]]:
    if sample & flag:
        print 'sample contains', name
    else:
        print 'sample does not contain', name
