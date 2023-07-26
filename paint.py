meter_carry = float(input("how many meter carry you paint? "))
area_paint_18l = 54
price = 80
cont = 0
if (meter_carry <= area_paint_18l):
    print("the price is ", price)
    print("you can paint ", meter_carry, "meter carry")
elif (meter_carry > area_paint_18l) and (meter_carry % area_paint_18l) == 0:
    cont=meter_carry/54
    print("the price is ", cont*price)
    print("you can paint ", meter_carry)
elif (meter_carry > area_paint_18l) and (meter_carry % area_paint_18l) >= 1:
    cont=int(meter_carry/54)
    print("the price is ", int(cont*price))
    print("you can print ", meter_carry)

    

