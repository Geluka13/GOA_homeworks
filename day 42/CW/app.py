age = int(input("Enter your age: "))

if age > 0:
    while age > 0:
        age = age // 2 
        print(age)
        age += age
        age = age // 2

else:
    print("Error")