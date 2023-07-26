number1 = int(input("write frist number "))
number2 = int(input("write second number "))
number3 = int(input("write third number "))
if ((number1 > number2) and (number1 > number3)):
    print("number 1 is more big")
elif ((number2 > number1) and (number2 > number3)):
    print("number 2 is more big")
else:
    print("number 3 is more big")