price1 = float(input("enter with the price 1 "))
price2 = float(input("enter with the price 2 "))
price3 = float(input("enter with the price 3 "))
if ((price1 < price2) and (price1 < price3)):
    print("the price 1 is more cheap")
elif ((price2 < price1) and (price2 < price3)):
    print("the price 2 is more cheap")
else:
    print("the price 3 is more cheap")