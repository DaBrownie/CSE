import random
round = 0
money = 15
broke = False

while money > 0 and broke is False:
    # question = input("Do you want to roll the dice?")
    # if question == "yes":
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    if die_1 + die_2 == 7:
        print("Congratz you have gained $4 and have %s" % money)
        print("You are on round %s" % round)
        print("You rolled %d" % (die_2 + die_1))
        round += 1
        money += 4
    elif die_1 + die_2 < 7:
        print("Try again you have lost $1 and have %s" % money)
        print("You are on round %s" % round)
        print("You rolled %d" % (die_2 + die_1))
        print(money - 1)
        print(round + 1)
        money -= 1
        round += 1
        if money == 0:
            print("You are out of money")
            broke = True
    elif die_1 + die_2 > 7:
        print("Try again you have lost $1 and have %s" % money)
        print("You are on round %s" % round)
        print("You rolled %d" % (die_2 + die_1))
        print(money - 1)
        print(round + 1)
        money -= 1
        round += 1
        if money == 0:
            print("You are out of money")
            broke = True