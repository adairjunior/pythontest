number1 = int(input("enter with the number 1 "))
number2 = int(input("enter with the number 2 "))
number3 = int(input("enter with the number 3 "))
if ((number1 > number2) and (number1 > number3) and (number2 > number3)):
    print("big to small is ", number1, number2, number3)
elif ((number2 > number1) and (number2 > number3) and (number1 > number3)):
    print("big to small is ", number2, number1, number3)
elif ((number3 > number1) and (number3 > number2) and (number1 > number2)):
    print("big to small is ", number3, number1, number2)
elif ((number1 > number2) and (number1 > number3) and (number3 > number2)):
    print("big to small is ", number1, number3, number2)
elif ((number2 > number1) and (number2 > number3) and (number3 > number1)):
    print("big to small is ", number2, number3, number1)
elif ((number3 > number1) and (number3 > number2) and (number2 > number1)):
    print("big to small is ", number3, number2, number1)
else:
    print("error in the system")