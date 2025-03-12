#1
age = input("enter your age: ")
print(int(age) > 13 < 19)
#2
math_score = input("enter your math exam score: ")
is_A = (int(math_score) >= 9)
is_B = (int(math_score) >= 8 <9)
is_C = (int(math_score) >= 7 < 8)
is_D = (int(math_score) >= 6 < 7)
is_F = (int(math_score) < 6)
print(is_A)
print(is_B)
print(is_C)
print(is_D)
print(is_F)
#3
variable1 = (7 > 4)
variable2 = (4 > 6)
print(int(variable1) > 1)
print(int(variable2) < 1)
print(int(variable1) == int(variable2))
#4
num1 = input("enter the first number: ")
num2 = input("enter the second number: ")
print(int(num1) == int(num2))
print(int(num1) < int(num2))
print(int(num1) > int(num2))
print(int(num1) <= int(num2))
print(int(num1) >= int(num2))
print(int(num1) != int(num2))
#5
a = 5
b = 7
c = 3
is_a_greatest = (a > b < a > c < a)
is_b_middle = (b > a < c > b)
is_c_least = (c < b > a > c)
#6
score = (70)
is_pass = (int(score) >= 50)
is_high_pass = (int(score) >= 75 < 90)
is_perfect = (int(score) == 100)
is_falling = (int(score) < 50)
#7
P = (5 > 3)
Q = (4 > 7)
P_and_not_Q = (5 < 7)
not_P_and_Q = (4 > 9)
P_xor_Q = (7 == 7)