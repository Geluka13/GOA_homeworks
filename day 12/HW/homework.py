#1
for i in range(1 , 50 , 2):
   print("goa")
print("-----------------")
goa = 0
while goa < 25:
   print("goa")
   goa += 1
print("-----------------")
#2
count = 4
while count < 7 :
    print("*" * 4)
    count += 1
print("------------------------------")
for i in range(3):
 print("*" * 4)
print("-----------------------------")
#3
count2 = 0
while count2 < 5:
   print("*" * 5)
   count2 += 1
print("--------------------------------")
for i in range(5):
   print("*" * 5)
print("----------------")
#4
num1 = 0
num = 1
for i in range(4) :
   for i in range(4):
      print(num1)
      print(num)
#5
password_enter = input("enter password: ")
password = "gela123"

while password_enter != password:
   password_enter = input("try again!: ")

print("log in succesfuly")