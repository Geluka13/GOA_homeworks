#2
def hello_world():
    hello_world2 = input("write hello_world: ")
    if hello_world2 == "hello_world":
        print("print()")
hello_world()
#3
def even_or_odd():
    even_or_odd = 24
    if even_or_odd % 2 == 0:
        print("ეს რიცხვი არ არის კენტი")
    else:
        print("ეს რიცხვი კენტია")
even_or_odd()
#4
def print_figures(x):
    for i in range(x):
        print("******")
    for i in range(x):
        print(" " * i + "******")
    for i in range(x):
        print(" " * ((5 - i) // 2) + "*" * i)
    for _ in range(x):
        print(" " * (5 // 2) + "*")
print_figures(120)