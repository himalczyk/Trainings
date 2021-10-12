
list_with_integers = [1,1,2,2,3]
list_some = []

for item in list_with_integers:
    if item in list_some:
        list_some.remove(item)
    else:
        list_some.append(item)

print(list_some)