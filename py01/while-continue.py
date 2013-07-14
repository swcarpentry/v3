num_moons = 5
while num_moons > 0:
    print 'top:', num_moons
    num_moons -= 1
    if (num_moons % 2) == 0:
        continue
    print '...bottom:', num_moons
