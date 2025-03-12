#1
arr2 = ["ა" , "ე" , "ბ" , "გ" , "დ" , "ზ" , "ი"]
ხმოვნები = "აეიოუ"
ხმოვნების_დათვლა = 0
for letters in arr2:
    for ხმოვანი in ხმოვნები:
        if letters == ხმოვანი:
            ხმოვნების_დათვლა += 1
print(ხმოვნების_დათვლა)
#2
numb = [5 , 9 ,10 , 12 ,  15 , 18 , 21 , 25]

for i in range(len(numb)):
    if numb[i] % 5 == 0:
        numb[i] = "5 is jeradi"
    else:
        numb[i] = "3 is jeradi"

print(numb)

#3

arr = [1 , "a" , 2 , "r" , 4 , 5 , "f" , "k" , "h" , "f" , 2 , 7 , 5 , 0]
result_string = ""

for i in arr:
    result_string += str(i)
print(result_string)

#4
fifqebi = "******"

for i in range(4):
    print(" " * i + fifqebi)

#5
age = input("enter your age: ")

if int(age) > 12:
    print("you are not 12 years old")