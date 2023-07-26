height = float(input("enter with the height "))
sex = str(input("enter with the sex "))
if (sex == "m") or (sex == "M"):
    weight = ((72.7*height)-58)
    print("the weight's man is ", weight)
elif (sex == "w") or (sex == "W"):
    weight = ((62.1*height)-44.7)
    print("the weight's woman is", weight)
