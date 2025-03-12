#1
sentence = "xinkali aris dzalian gemrieli"
res = []
word = ""
delimter = " "
for char in sentence:
    if char == delimter:
        if word:
            res.append(word)
            word = ""

    else:
        word += char

if word:
    res.append(word)
print(res)

#2
sentence2 = ['xinkali', 'aris', 'dzalian', 'gemrieli']
res2 = ""
delimter2 = " "
for i in sentence2:
    if i > str(0):
        res2 += delimter2
    res2 += i
print(res2)

#3
sentence3 = "me minda vasli"
new = "me minda banani"
res3 = ""
for i in range(1):
    if sentence3 == new:
        print("me minda vasli")
    else:
        res3 += new
print(res3)

#4
num1 = input("enter first num: ")
num2 = input("enter second num: ")
operation = input("enter operation (+,-,*,/): ")

if operation == "+":
    print(int(num1) + int(num2))
if operation == "-":
    print(int(num1) - int(num2))
if operation == "*":
    print(int(num1) * int(num2))
if operation == "/":
    print(int(num1) / int(num2))

#5
words = input("enter as many words as you want: ")
arr = [words]
joined_arr = " ".join(arr)
print(joined_arr)