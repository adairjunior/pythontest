number = (int)(input('enter with one number '))
if ((number > 0) and (number < 1000)):
    if (number <= 9):
        print("the number unit is ", number)
    elif ((number >= 10) and (number <= 99)):
        if ((number%2)==0) or ((number%2)==1):
            print("the dezene number is ", number)
    elif ((number >= 100) and (number <= 999)):
        if ((number%2)==0) or ((number%2)==1):
            print("the centeine number is ", number)


