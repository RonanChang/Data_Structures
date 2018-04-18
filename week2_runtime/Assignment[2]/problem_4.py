#The runtime of the follow algorithm is O(NlogN)
#N is the size of the largest set among A,B,C

def Disjoint(A,B,C):
    myList = list(A) + list(B) + list(C)
    
    sorted_list = mergeSort(myList)
    
    i = 0
    while i < len(sorted_list)-2:
        if sorted_list[i] != sorted_list[i + 1]:
            i += 1
            continue
        if sorted_list[i + 1] == sorted_list[i + 2]:
            return False
        else:
            i += 2
    return True

    

def mergeSort(lst):
 
    if len(lst)>1:
        mid = len(lst)//2
        lefthalf = lst[:mid]
        righthalf = lst[mid:]

        lefthalf = mergeSort(lefthalf)
        righthalf = mergeSort(righthalf)
        
        return merge(lefthalf,righthalf)
    return lst
        
def merge(lefthalf,righthalf):
    new_lst = []
    i=0
    j=0

    
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            new_lst.append(lefthalf[i])
            i=i+1
        else:
            new_lst.append(righthalf[j])
            j=j+1
     

    while i < len(lefthalf):
        new_lst.append(lefthalf[i])
        i=i+1
     
    while j < len(righthalf):
        new_lst.append(righthalf[j])
        j=j+1
    
    return new_lst
       

#return True if they are disjoint, return False if they are not disjoint    
print(Disjoint({3,2},{7,2},{8,2}))
print(Disjoint({1,2},{7,5},{8,0}))