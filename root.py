print("ax2 + bx + c")
a = int(input("enter with A "))
if (a == 0):
    print("the equation dont second level")
else:
    if (a != 0):
        b = int(input("enter with B "))
        c = int(input("enter with C "))
        print("here is ok")
        delta = b**2 - 4*a*c
        if (delta < 0):
            print("not root real")
        elif (delta == 0):
            x = (-b)/(2*a)
            print ("the equation has 1 root real ")
            print(x)
            m=0
        elif (delta > 0):
            print("the equation is" , a,'x2', '+', b,'x' ,'+', c)


