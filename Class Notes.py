# Defining a class
class Shoes(object):
    def __init__(self, lace_color, lighting, brand):  # TWO underscores before and after
        # Things a shoe has
        self.laces_color = lace_color
        self.rgb_lighting = lighting
        self.used = False
        self.brand = brand
        self.clean = True

    def wear(self):
        self.used = True
        self.clean = False
        print("You wear the shoes")

    def wash(self):
        self.clean = True
        print("You clean the shoes")


first_pair = Shoes("Red", True, "Jordan")
second_pair = Shoes("Pink", False, "Sketchers")

print(first_pair.brand)
print(second_pair.laces_color)
print(first_pair.clean)

first_pair.wear()
print(first_pair.clean)
first_pair.wash()
print(first_pair.clean)


class Car(object):
    def __init__(self, name, type, color, horsepower):
        self.type = type
        self.color = color
        self.name = name
        self.horsepower = horsepower
        self.wash = True
        self.passengers = 0
        self.running = False

    def wash(self):
        self.wash = True
        print("You wash the car")

    def drive_foward(self):
        if self.running:
            print("You move forward")
        else:
            print("Nothing Happens")

    def turn_on(self):
        if self.running:
            print("Nothing Happens")
        else:
            self.running = True
            print("You start the car")

    def turn_off(self):
        if self.running:
            self.running = False
            print("You turn the car off")
        else:
            print("Noting happens")

    def go_for_drive(self, passengers):
        print("%d passengers get in" % passengers)
        self.passengers = passengers
        self.turn_on()
        self.drive_foward()
        self.drive_foward()
        self.drive_foward()
        self.turn_off()
        print("%d passengers get out" % passengers)
        self.passengers = 0


my_car = Car("Pagani Zonda", "R", "Red", 9000.01)
my_car.go_for_drive(4)