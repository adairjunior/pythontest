note1 = (float)(input("enter with firt note "))
note2 = (float)(input("enter with second note "))
note3 = (float)(input("enter with third note "))
media = (note1+note2+note3)/3
if (media >= 7) and (media != 10):
    print("student approved")
elif (media < 7):
    print("student reproved")
elif (media == 10):
    print("excellent")
