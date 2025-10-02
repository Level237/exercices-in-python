
def sortListTuplesByLastElement(list:list):
     return sorted(list, key=lambda x: x[-1]);

print(sortListTuplesByLastElement([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))