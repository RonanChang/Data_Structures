Student Name: Ruonan Chang(rc3477)
==========================================================
Problem_1:

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

==========================================================
Problem_2:


#The runtime of the function below is O(N)

def LargestTen(lst):
    copy = lst[::]
    ten = []
    
    for i in range(10):
        Max = copy[0]
        for j in copy[1:]:
            if j > Max:
                Max = j
        
        #the runtime of remove() is O(n)
        ten.append(Max)
        copy.remove(Max)
    return ten

print(LargestTen([1,2,3,76,5,6,7,8,9,0,89]))

=========================================================
Problem_3:

#The runtime of this function is O(N)
def Search(lst):
    n = len(lst)
    total_of_range = n*(n+1)/2
    total_of_lst = sum(lst)
    missing_num = total_of_range - total_of_lst
    return int(missing_num)

lst = [0,1,3,4,5,6]
print(Search(lst))

=========================================================
Problem_4:
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

=========================================================
Problem_5:

import math

'''
Look at the example as below:
    when n is not large enough(knowing from the prompt that when n < 100):
    if we add a relatively large number to N*logN, 
    or if the coeffient of n**2 is a relatively small number,
    then the actual runtime will be N * logN > N**2
    
    However, due to the nature of Big-O notation, 
    we ignore the constant number and the coeffient number,
    and that causes the confusion. 
    
'''
n = 50
print("n * math.log(n) + 1500 = " + str(n * math.log(n) + 1500))
print("0.5 * n**2 = " + str(0.5 * n **2))

m = 150
print("m * math.log(m) + 1500 = " + str(m * math.log(m) + 1500))
print("0.5 * m**2 = " + str(0.5 * m **2))

=========================================================
Problem_6:

def MinMax(lst):
    mins = []
    maxs = []
    
    #The number of comparisons of the first for loop is N/2
    for i in range(0, len(lst), 2):
        if lst[i] < lst[i+1]:
            mins.append(lst[i])
            maxs.append(lst[i + 1])
    
    #The number of the comparisons of the second for loop is N/2
    Min = mins[0]
    for i in range(len(mins)):
        if mins[i] < Min:
            Min = mins[i]
    
    #The number of comparisons of the third for loop is N/2
    Max = maxs[0]
    for i in range(len(maxs)):
        if maxs[i] > Max:
            Max = maxs[i]
    
    return Min, Max

#Suppose the length of the list is always even
print(MinMax([2,5,33,435,3,8]))