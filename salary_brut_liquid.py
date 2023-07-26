hour_pay = float(input("enter with the hour's pay "))
hour_week = float(input("enter with the hour's work week "))
hour_month = hour_week*4
salary_brut = hour_pay * hour_month
inss = salary_brut*0.08
IR = salary_brut*0.11
sindicaty = salary_brut*0.05
salary_liquid = salary_brut - inss - IR - sindicaty
print("you salary brut is ", salary_brut)
print("you pay bill's inss ", inss)
print("you pay bill's tax ", IR)
print("you pay bill's sindicaty ", sindicaty)
print("you salary liquid is ", salary_liquid)
