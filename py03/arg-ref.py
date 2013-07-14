def add_salt(first, second):
    first += "salt"
    second += ["salt"]

str = "rock"
seq = ["gneiss", "shale"]

print "before"
print "str is:", str
print "seq is:", seq

add_salt(str, seq)

print "after"
print "str is:", str
print "seq is:", seq

