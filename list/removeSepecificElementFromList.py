

def removeSepecificElementFromList(startList:list,elements:list):
    position=list(startList)
    for j in elements:
        for index,i in enumerate(startList):
            if(index==j):
                position.remove(i)
           
    return position;

print(removeSepecificElementFromList(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'],[2,5]))