import re

# main:start
assert re.search('AC?T', 'AT')
assert re.search('AC?T', 'ACT')
assert not re.search('AC?T', 'ACCT')
# main:end
