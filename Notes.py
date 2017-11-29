# print("Hello World")
#
# # Azrael
#
#
# print(3+5)
# print(5-3)
# print(3*5)
# print(6/2)
# print(3**2)
#
# print() # this makes a a new line. In python 3.6, it looks like: print()
# print("See if you can figure this out")
# print(5%3)
#
# car_name = "Wiebe Mobile"
# car_type = "Lamborghini Sesta Elemento"
# car_cylinders = 8
# car_mpg = 9000.1
#
# # Inline printing
# print("I have car called the %s" % car_name)
# print("I have a car called the %s. It's a %s." % (car_name, car_type))
#
# #Asking for input
# name = input("what is you name? ") #In python 3, its just called input()
# print("Hello %s." % name)
#
# age = input("how old are you?")
# print(" %s...........Wow that's really old." % age)

#Functions


def print_hw():
    print("Hello World")


print_hw()
print_hw()
print_hw()


def say_hi(name):   # "(name)" is a Parameter
    print("Hello %s." % name)
    print("Enjoy your day.")


say_hi("John")


def print_age(name, age):
    print("%s is %d years old." % (name, age))
    age += 1 # age = age + 1
    print("Next year, they will be %d" % age)


print_age("John", 15)


def f(x):
    return x**3 + 4 * x**2 + 7 * x - 4


print(f(3))
print(f(4))
print(f(5))


# If statements


def grade_calc(percemtage):
    if percentage >= 90:
        return "A"
    elif percentage >=80 :
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage <= 50:
        return "F"
    