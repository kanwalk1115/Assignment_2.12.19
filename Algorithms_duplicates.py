
names= ["Alex", "John", "Mary", "Steve", "John", "Steve"]

def remove_duplicates(list):
    newlist= []
    for name in list:
        if name not in newlist:
            newlist.append(name)
    return newlist

print(remove_duplicates(names))
