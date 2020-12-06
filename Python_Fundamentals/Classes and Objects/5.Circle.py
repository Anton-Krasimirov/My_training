class Circle:
    __pi = 3.14
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):# izchislqvame obikolkata
        return Circle.__pi * self.diameter

    def calculate_area(self):# ploshta
        return Circle.__pi * self.radius * self.radius

    def calculate_area_of_sector(self, angle):
        return (angle/360) * Circle.__pi * self.radius * self.radius

circle = Circle(10)
angle = 5




print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")

# diameter d=2*r  diametar e input
# circumference- obikolka P = 2*pi*r
# area-lice S = pi*r**2
# area of sector-lice na sektor  , sector e angle-ъгъл , angle e input
# area of ange S = pi * r ** 2    (input/360) * pi * r * r
# radius = diameter / 2
