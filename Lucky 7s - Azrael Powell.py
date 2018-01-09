import random
round = 0
money = 15
die_1 = random.ranint(1, 6)
die_2 = random.ranint(1, 6)

while money > 0:
    print =("You have rolled the dice")
    print(die_1)
    print(die_2)
    dice = print(die_1 + die_2)
    if dice == 7:
        print("Congratz you have gained $4")
        print(money + 4)
    elif dice < 7:
        print("Try again")
        print(money - 1)
    elif dice > 7:
        print("Try again")
        print(money - 1)