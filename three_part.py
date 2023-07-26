part1 = int(input("enter with part 1 "))
part2 = int(input("enter with part 2 "))
part3 = int(input("enter with part 3 "))
if (part1+part2 > part3) and (part1+part3 > part2) and (part2+part3 > part1):
    print("é triangulo")
    if (part1 == part2) and (part2 == part3):
        print("trinagulo equilatero")
    elif ((part1 == part2) and (part1 != part3)) or ((part1 == part2) and (part2 != part3)) or ((part2 == part3) and (part2 != part1)) or ((part1 == part3) and (part2 != part1)):
        print("triangulo isoceles")
    elif ((part1 !=  part2) and (part1 != part3)):
        print("é triangulo escaleno")
else:
    print("não é triangulo")