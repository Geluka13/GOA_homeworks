#1
list_of_names = ["gela" , "davit" , "sandro" , "nika" , "gio" , "davit"]
print(list_of_names.count("davit"))
#2
list_of_numbs = [1 , 2 , 4 , 3 , 5 , 5 , 2 , 8]
list_of_numbs.reverse()
print(list_of_numbs)
#3
list_of_numbs2 = [1, 2, 3,]
list_of_numbs3 = []
for i in list_of_numbs2:
    list_of_numbs3 += list_of_numbs2
print(list_of_numbs3)
#4
insert_arr = ["gio", "gurami" , "tamazi"]
insert_arr.insert(3, "daviti")
print(insert_arr)
#5
arr = [1, 2 , 4 , 7 , 8, 3, 9 , 6]
print(arr.count(2))
arr.remove(2)
print(arr)