# Dictionary Methods 
ep = {
    1:23,
    2:34,
    3:35,
    4:67,
    5:80,
    6:79,
    7:90,
    8:100,
    9:10
}

ep_mg = {
    10:90,
    11:90
}

# update()
ep_mg.update(ep)
print(ep_mg)

# clear()
ep.clear()
print(ep)

# pop()
ep_mg.pop(10)
print(ep_mg)

# popitem()
ep_mg.popitem()
print(ep_mg)

