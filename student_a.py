note1 = float(input("enter with note 1 "))
note2 = float(input("enter with note 2 "))
media = (note1 + note2)/2
if ((media >=0) and (media <= 4)):
    print("the note 1 is ", note1)
    print("the note 2 is ", note2)
    print("the media is ", media)
    print("you are reproved - E")
elif ((media > 4) and (media < 6)):
    print("the note 1 is ", note1)
    print("the note 2 is ", note2)
    print("the media is ", media)
    print("you are reproved - D")
elif ((media >= 6) and (media < 7.5)):
    print("the note 1 is ", note1)
    print("the note 2 is ", note2)
    print("the media is ", media)
    print("you are approved - C")
elif ((media >= 7.5) and (media < 9)):
    print("the note 1 is ", note1)
    print("the note 2 is ", note2)
    print("the media is ", media)
    print("you are Approved - B")
elif ((media >= 9) and (media <= 10)):
    print("the note 1 is ", note1)
    print("the note 2 is ", note2)
    print("the media is ", media)
    print("you are Approved - A")
else:
    print("note invalid")