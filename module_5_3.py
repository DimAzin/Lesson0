class Building:
    def __init__(self, buildingType, numberOfFloors):
        self.buildingType = buildingType
        self.numberOfFloors = numberOfFloors

    def __eq__(self, other):
        if self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType:
            return  True
        else:
            return False


h1 = Building('Кузнечики', 3)
h2 = Building('Домострой', 5)
h3 = Building('Домострой', 5)

print(h1 == h2)
print(h2 == h3)
