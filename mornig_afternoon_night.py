day = str(input("enter with M - morning A - afternoon - N - night "))
if ((day == 'M') or (day == 'm')):
    print("good morning")
elif ((day == 'A') or (day == 'a')):
    print("good afternoon")
elif ((day == 'N') or (day == 'n')):
    print("good night")
else:
    print("unknow code")