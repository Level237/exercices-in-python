
def getCountSameStringInStartAndEnd(list):
    counter=0;
    for word in list:
        if(len(word)> 1 and word[0]==word[-1]):
            counter+=1
    return counter;

print(getCountSameStringInStartAndEnd(['abc','xyz','aba','1221']))