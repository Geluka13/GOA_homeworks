#1
set1 = {"apple" , "pineapple" , "cherry"}
set1.add("watermelon")
print(set1)
set1.remove("apple")
print(set1)
set1.clear()
print(set1)
set2 = {"pineapple" , "strawberry" , "blueberry" , "watermelon"}
set1.difference(set2)
set3 = set1.union(set2)
print(set3)
#2
me = {
    "name" : "Gela",
    "surname" : "Genebashvili",
    "age" : 14,
    "academy" : "GOA"
}
me_keys = me.keys()
print(me_keys)
#2
me_values = me.values()
print(me_values)
#3
def AddToDatabase(database, name, surname, age):
    user_id = len(database) + 1  
    database[user_id] = {"Name": name, "Surname": surname, "Age": age}
    print(f"Added to database: {database[user_id]}")
    return database


database = {}


database = AddToDatabase(database, "khvicha", "kvarastkhelia", 28)
database = AddToDatabase(database, "guram", "kashia", 35)

print(database)