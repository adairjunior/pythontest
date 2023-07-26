size_MB = float(input("Wha is the size in MB "))
link = float(input("What is the internet link? "))
result = (size_MB / (link/8))
minute = result*60
print("the link is ", result, "second")
print("the link is ", minute, "minute")
