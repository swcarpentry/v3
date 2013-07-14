num_moons = 3
while True:             # Looks like an infinite loop...
    print num_moons
    num_moons -= 1
    if num_moons <= 1:
        break           # ...but there's a way out
