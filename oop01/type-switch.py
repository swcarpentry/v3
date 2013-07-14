# main:start
for time in simulation_period:
    for thing in world:
        if type(thing) is plant:
            update_plant(thing, time)
        elif type(thing) is fish:
            update_fish(thing, time)
        elif type(thing) is creepy_crawly:
            update_creepy_crawly(thing, time)
# main:end
