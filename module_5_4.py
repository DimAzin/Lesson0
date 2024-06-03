class Building:
    total = 0
    def __init__(self):
        Building.total += 1

h = []
for i in range(40):
    h.append(Building())
    print(h[i].total)

for i in range(40):
    print(h[i].total)