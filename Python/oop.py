class Dog():
    # class object attribute
    species = 'Mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


mydog = Dog('Labrador', 'Sammy')

class Circle():

    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2

    def set_radius(self, new_radius):
        self.radius = new_radius


mycircle = Circle(3)
print(mycircle.area())
mycircle.set_radius(15)
print(mycircle.area())
