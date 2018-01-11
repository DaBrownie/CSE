import random
round = 0
money = 15
broke = False
tm = 0  # tm stands for "Top Money"
tr = 0  # tr stands for "Top Round"

while money > 0 and broke is False:
    D1 = random.randint(1, 6)
    D2 = random.randint(1, 6)
    if D1 + D2 == 7:
        print("You rolled %d" % (D2 + D1))
        money += 4
        print("Congratz you have gained $4 and have $%s" % money)
        round += 1
        print("You are on round %s" % round)
        print()
        # if money > 15:
        #     question = input("Do you want to stop?")
        #     if question == "yes":
        #         broke = True
        #         print("You got to round %s" % round)
        #     if question == "no":
        #         broke = False
    elif D1 + D2 != 7:
        print("You rolled %d" % (D2 + D1))
        money -= 1
        print("You have lost $1 and have $%s" % money)
        round += 1
        print("You are on round %s" % round)
        print()
        if money == 0:
            print("You are out of money")
            print("You got to %s" % round)
            broke = True
            print("You should have stopped at round %s when you had $%s" % (tr,tm))
    if money > tm:
        tm = money
        tr = round