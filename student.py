note1 = float(input("enter with note 1 "))
note2 = float(input("enter with note 2 "))
media = (note1 + note2)/2
if (media >= 7) and (media < 10):
    print("approved")
elif (media < 7):
    print("reproved")
elif (media == 10):
    print("you are top")