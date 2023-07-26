how_many_your_hour = float(input("How many your hour? "))
how_many_work_week = float(input("How many your work at week? "))
salary_full = how_many_your_hour * (how_many_work_week*4)
if (salary_full <= 900):
    sind = salary_full * 0.03
    fgts = salary_full * 0.11
    salary_net = salary_full - sind
    print("the salary with FGTS is ", fgts)
    print("the salary net is ", salary_net)
elif ((salary_full > 900) and (salary_full <=1500)):
    sind = salary_full * 0.03
    revenu = salary_full * 0.05
    fgts = salary_full * 0.11
    salary_net = salary_full - sind - revenu
    print("the salary with FGTS is ", fgts)
    print("the salary net is ", salary_net)
elif ((salary_full > 1500) and (salary_full < 2500)):
    sind = salary_full * 0.03
    revenu = salary_full * 0.10
    fgts = salary_full * 0.11
    salary_net = salary_full - sind - revenu
    print("the salary with FGTS is ", fgts)
    print("the salary net is ", salary_net)
elif (salary_full > 2500):
    sind = salary_full *0.03
    revenu = salary_full * 0.20
    fgts = salary_full * 0.11
    salary_net = salary_full - sind - revenu
    print("the salary with FGTS is ", fgts)
    print("the salary net is ", salary_net)
else:
    print("system is error")