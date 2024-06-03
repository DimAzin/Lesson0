class House:
    def __init__(self, name):
        self.name = name
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

h1 = House('Кузнечики')
h1.setNewNumberOfFloors(5)