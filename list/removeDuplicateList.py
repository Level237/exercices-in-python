
def removeDuplicateList(list:list):
    newList=[]
    for i in list:
        if i not in newList:
            newList.append(i)
    return newList;

print(removeDuplicateList([1,1,3,4,4,5]))