number1 = int(input("enter with number 1 "))
number2 = int(input("enter with number 2 "))
number3 = int(input("enter with number 3 "))
if ((number1 > number2) and (number1 > number3) and (number2 > number3)):
    print("the big number is ", number1)
    print("the small number is ", number3)
elif((number2 > number1) and (number2 > number3) and (number1 > number3)):
    print("the big number is ", number2)
    print("the small number is ", number3)
elif ((number3 > number1) and (number3 > number2) and (number2 > number1)):
    print("the big number is ", number3)
    print("the small number is ", number1)
elif ((number1 > number2) and (number1 > number3) and (number3 > number2)):
    print("the big number is ", number1)
    print("the small number is ", number2)
elif ((number2 > number1) and (number2 > number3) and (number3 > number1)):
    print("the big number is ", number2)
    print("the small number is ", number1)
elif((number3 > number1) and (number3 > number2) and (number1 > number2)):
    print("the big number is ", number3)
    print("the small number is ", number2)
else:
    print("error in the system")