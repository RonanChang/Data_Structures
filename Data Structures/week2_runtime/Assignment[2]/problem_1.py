
#The runtime of this function is O(N)
def merge(list1, list2):
    list0 = []
    list1 = iter(list1)
    list2 = iter(list2)

    while True:
        failed = 0
        try:
            list0.append(next(list1))
        except:
            failed+=1

        try:
            list0.append(next(list2))
        except:
            failed+=1

        if failed == 2:
            break

    return list0

print(merge(range(3),range(3,11)))
print(merge(range(5),range(100,101)))
print(merge(range(1),range(100,105)))



      
       