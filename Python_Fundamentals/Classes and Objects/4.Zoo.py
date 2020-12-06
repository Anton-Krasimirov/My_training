class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, spicies, name):
        if spicies == "mammal":
            self.mammals.append(name)
        elif spicies == "fish":
            self.fishes.append(name)
        elif spicies == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, the_spicies):
        if the_spicies == "mammal":
            name_m = self.mammals
            return f"Mammals in {zooname}: {', '.join(name_m)}\nTotal animals: {self.__animals}"
        if the_spicies == "fish":
            name_m = self.fishes
            return f"Fishes in {zooname}: {', '.join(name_m)}\nTotal animals: {self.__animals}"
        if the_spicies == "bird":
            name_m = self.birds
            return f"Birds in {zooname}: {', '.join(name_m)}\nTotal animals: {self.__animals}"


zooname = input()
zoo = Zoo(zooname)
n = int(input())

for _ in range(n):
    spicies, name = input().split(" ")
    zoo.add_animals(spicies, name)

the_spicies = input()

print(zoo.get_info(the_spicies))
