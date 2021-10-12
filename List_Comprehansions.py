# list_comprehension = [1, 7, 5, 3, 2]

# comprehended_list = [multiplied*7 for multiplied in list_comprehension]

# print(comprehended_list)

def intersection(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3

list1 = [2, 42, 48, 62, 28, 3]
list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]
print(intersection(list1, list2)) #prints only the same values that appeared

#intersection function to use built in python

def return_intersection(list1, list2):
    set1= set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

list1 = [2, 43, 48, 62, 64, 28, 3]
list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]
new_list = return_intersection(list1, list2)
print(new_list)