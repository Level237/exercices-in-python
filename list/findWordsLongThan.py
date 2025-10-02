
def findWordsLongThan(list:list,n):
    copyList=[];
    for i in list:
        if(len(i)>n):
            copyList.append(i)
    return copyList;

print(findWordsLongThan(['abc','xyz','aba','1221'],2))