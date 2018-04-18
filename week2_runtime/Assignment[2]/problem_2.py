
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
    
    
    
    
    
    