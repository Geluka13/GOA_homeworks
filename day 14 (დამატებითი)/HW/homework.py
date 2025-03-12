#1
name = input("enter your name: ")
result = ""
for i in name:
    name += result
    print(i)
print(result)
#2
დიაპაზონი = input("From where to where to write the range of numbers: ")
if int(დიაპაზონი) // 2 and 3:
    print("this numbers are Multiples of 2 and 3")
else:
    print("thanks")
#3
for i in range(5):
    numbers = input("enter numbers: ")
print(int(numbers) + int(numbers) + int(numbers) + int(numbers) + int(numbers) / 5)
#4
for i in range(-100, 100, 100):
    print(int(i) + 100)
#5
num1 = input("enter the positive number: ")
while int(num1) <= 0:
    num1 = input("try again!: ")
print("correct number!")