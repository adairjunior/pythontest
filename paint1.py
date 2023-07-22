meter_carry = float(input("What is the meter carry "))
buy = input("Chosse box or box1 or box2")
area_paint_18l = 108
area_paint_6 = 21.6
area_paint_4 = 24
cont = 1
price = 80
price_big_box = 25
if (buy == "box"):
    if (meter_carry <= (area_paint_18l)):
        cont=1
        print ("you need", cont, "paint box")
        print("the price is", price)
    elif ((meter_carry) <= (area_paint_18l)) and (meter_carry % area_paint_18l)==0:
        cont = meter_carry / area_paint_18l
        price = cont * price
        print("you need ", cont , "paint box")
        print("the price is", price)
    elif (meter_carry > area_paint_18l) and ((meter_carry % area_paint_18l)!=0):
        cont = (int(meter_carry / area_paint_18l))
        cont+=1
        price = cont * price
        print("you need", cont , "paint box")
        print("you will use", meter_carry, "litre")
        print("the price is", price)
    elif (meter_carry > area_paint_18l) and ((meter_carry % area_paint_18l)==0):
        cont = (int(meter_carry / area_paint_18l))
        cont+=1
        price = cont * price
        print("you need", cont , "paint box")
        print("you will use", meter_carry, "litre")
        print("the price is", price)
elif (buy == "box1"):
    if (meter_carry <= (area_paint_6)):
        cont=1
        print ("you need", cont, "paint big box")
        print("the price is", price_big_box)
    elif (meter_carry > area_paint_6) and ((meter_carry % area_paint_6)!=0):
        cont = (int(meter_carry / area_paint_6))
        cont+=1
        price_big_box = cont * price_big_box
        print("you need", cont , "paint box")
        print("you will use", meter_carry, "litre")
        print("the price is", price_big_box)
    elif (meter_carry > area_paint_6) and ((meter_carry % area_paint_6)==0):
        cont = (int(meter_carry / area_paint_6))
        price_big_box = cont * price_big_box
        print("you need", cont , "paint box")
        print("you will use", meter_carry, "litre")
        print("the price is", price_big_box)
elif (buy == "box2"):
    if (meter_carry < 72):
        cont=+3
        print("you need", cont, "paint box")
        print("the price is", cont*price_big_box)
    elif (meter_carry >= 72) and (meter_carry <= 108):
        print("you need", cont, "paint box")
        print("the price is", price)
    elif (meter_carry > 24) and (meter_carry <= area_paint_18l):
        print("you need", cont, "paint box")
        print("the price is", price)
    else:
        print("problem in the system")





