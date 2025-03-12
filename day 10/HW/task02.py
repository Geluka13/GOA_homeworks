#1
age = input("enter your age: ")
for iteration in range(5):
    print(age);
#2
temp = input("enter temperature in Celsius: ")
print(int(temp) * 9/5 + 32)
#3
print(True or False)
print(True and True)
print(False or False)
print(5 >= 5)
print(3 == 2)
print(7 >= 9)
#4
rows = 5  # Number of rows in the pyramid

for i in range(rows):
    print(' ' * (rows - i - 1), end='')
    print('❤ ' * (i + 1))
 

#5
age2 = input("enter your age: ")
visitor_age = (int(age2) == 20)
print(visitor_age)