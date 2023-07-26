salary = float(input("enter with the salary "))
salary_full = 0.0
if ((salary > 0) and (salary <= 280)):
    salary_full = salary + (salary * 0.20)
    print("before salary", salary)
    print("the % about salary is 20%")
    print("the amount add salary is", salary * 0.20)
    print("the new salary is ", salary_full)
elif ((salary > 280) and (salary <= 700)):
    salary_full = salary + (salary * 0.15)
    print("before salary", salary)
    print("the % about salary is 15%")
    print("the amount add salary is", salary * 0.15)
    print("the new salary is ", salary_full)
elif ((salary > 700) and (salary <= 1500)):
    salary_full = salary + (salary * 0.10)
    print("before salary", salary)
    print("the % about salary is 10%")
    print("the amount add salary is", salary * 0.10)
    print("the new salary is ", salary_full)
elif ((salary > 1500)):
    salary_full = salary + (salary * 0.05)
    print("before salary", salary)
    print("the % about salary is 5%")
    print("the amount add salary is", salary * 0.05)
    print("the new salary is ", salary_full)
else:
    print("salary invalid")