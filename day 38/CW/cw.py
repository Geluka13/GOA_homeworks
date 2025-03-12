#1
def manual_difference():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    result = set()
    for item in set1:
        if item not in set2:
            result.add(item)
    return result

result = manual_difference()
print("Manual Difference:", result) 

#2
student1 = {
    "name": "giorgi",
    "surname": "mikautadze",
    "age": 15,
    "score": 9.2
}
student2 = {
    "name": "khvicha",
    "surname": "kvaratskhelia",
    "score": 10
}
print(student1)
print(student2)