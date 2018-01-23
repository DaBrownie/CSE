import string
# import random  # This should be on line #1
#  print("Hello World")
# Azrael
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
# Inline printing
# print("I have car called the %s" % car_name)
# print("I have a car called the %s. It's a %s." % (car_name, car_type))
# Asking for input
# name = input("what is you name? ")  # In python 3, its just called input()
# print("Hello %s." % name)
#
# age = input("how old are you?")
# print(" %s...Wow that's really old." % age)
#
# Functions
#
#
# def print_hw():
#     print("Hello World")
#
#
# print_hw()
# print_hw()
# print_hw()
#
#
# def say_hi(name):   # "(name)" is a Parameter
#     print("Hello %s." % name)
#     print("Enjoy your day.")
#
#
# say_hi("John")
#
#
# def print_age(name, age):
#     print("%s is %d years old." % (name, age))
#     age += 1  # age = age + 1
#     print("Next year, they will be %d" % age)
#
#
# print_age("John", 15)
#
#
# def f(x):
#     return x**3 + 4 * x**2 + 7 * x - 4
#
#
# print(f(3))
# print(f(4))
# print(f(5))
#

# If statements


# Loops
#
#
# for num in range(1000000):
#    print(num + 1)
#
# DO NOT RUN!!!
# a = 1
# while True:
#    print(a)
#
#
# a = 1
# while a < 10:
#     print(a)
#     a += 1
#
#
# Random Numbers
#
# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     elif percentage <= 50:
#         return "F"
#
# print(random.randint(0, 100))


# Lists
# the_count = (1, 2, 3, 4, 5)
# shopping_list = ["Noodles", "Eggrolls", "Milk", "Rice", "Soda", "Chips"]
#
# print(shopping_list[2])
#
# print(len(shopping_list))
#
# # Going through a list
# for item in shopping_list:
#     print(item)
#
# for(num) in the_count:
#     print(num * 2)
#
# len(shopping_list)   # Gives me the length of the list
# range(3)  # Gives you the range of of numbers 0 through 2 but never the actual number
# range(len(shopping_list))  # A list of EVERY index in a list
#
# for num in range(len(shopping_list)):
#     item = shopping_list[num]
#     print("The item at index %d is %s" % (num, item))
#
#
# # Turns things into a list
# str1 = "Hello Class!"
# ListOne = list(str1)
# print(ListOne)
# ListOne[11] = '.'
# print(ListOne)
# print("".join(ListOne))
#
# # Add things to a list
# shopping_list.append("Cereal")
# print(shopping_list)
#
# # Removing things from a list
# shopping_list.remove("Soda")
# print(shopping_list)
# shopping_list.pop(0)
# print(shopping_list)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.punctuation)
# print(string.digits)
#
# # Dealing with strings
# strTwo = "ThIs iS a VeRY oDd sEnTenCE"
# lowercase = strTwo.lower()
# print(lowercase)