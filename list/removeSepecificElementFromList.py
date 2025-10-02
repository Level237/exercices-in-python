

def removeSepecificElementFromList(list:list,elements:list):
    for i in list:
        for j in elements:
            if i==j:
                list.remove(i)
    return list;

print(removeSepecificElementFromList([1,2,3,4,5],[3,5]))