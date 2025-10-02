
def checkCommonMemberBetweenTwoList(list1:list,list2:list):
    for i in list1:
        for j in list2:
            if i==j:
                return True;

print(checkCommonMemberBetweenTwoList([1,2,3,9,5],[6,7,8,9,10]))