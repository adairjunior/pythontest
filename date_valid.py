date_day = int(input("enter with the day "))
date_month = int(input("enter with the month "))
date_year = int(input("enter with the year "))
if (date_day > 0) and (date_day < 32):
    if (date_month > 0) and (date_month < 13):
        if (date_year > 0):
            print("date valid")