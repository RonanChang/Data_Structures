
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
        
            
        