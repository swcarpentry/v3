import re

# main:start
assert re.search('TTAG*CTA', 'TTACTA')
assert not re.search('TTAG+CTA', 'TTACTA')
# main:end
