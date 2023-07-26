money = (float(input(" what is the amount you would like take? ")))
if (money == 1):
    print("You have 1 dolar")
elif (money == 5):
    print("you have 5 dolar")
elif (money == 10):
    print("you have 10 dolar")
elif (money == 50):
    print("you have 50 dolar")
elif (money == 100):
    print("you have 100 dolar")
else:
    if ((money > 1) and (money < 5)):
        if (money == 2):
            print("you take 2 paper 1 dollar")
        elif (money == 3):
            print("you have 3 paper 1 dollar")
        elif (money == 4):
            print("you have 4 paper 1 dollar")
    elif ((money > 5) and (money < 10)):
        if (money == 6):
            print("you have 1 paper 5 dolar and 1 paper 1 dolar")
        elif (money == 7):
            print("you have 1 paper 5 dolar and 2 paper 1 dolar")
        elif (money == 8):
            print("you have 1 paper 5 dolar and 3 paper 1 dolar")
        elif (money == 9):
            print("you have 1 paper 5 dolar and 4 paper 1 dolar")
