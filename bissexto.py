year = int(input("write the year? "))
if (((year%400)==0) and ((year%4)==0)):
    print("year bissext")
#elif (((year%400)==0) and ((year%4)==0)) and ((year%100)==0):
#    print("year not bissext")
elif (((year%400)==0) or ((year%4)==0)) and ((year%100)==0):
    print("year not bissext")


