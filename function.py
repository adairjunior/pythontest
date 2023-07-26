def old_year (name, age):
    if (age <= 18):
        return f' The teen with name {name} have {age}'
    elif (age > 18) & (age < 65):
        return f'the adult with name {name} have {age}'
    else:
        return f'the oldest with name {name} have {age}'
if __name__ == '__main__':
    print(old_year('adair', 90))
    print(old_year('atair', 5))
    print(old_year('alana', 32))
