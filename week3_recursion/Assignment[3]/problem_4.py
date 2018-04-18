#The runtime of this metho is O(n^2)
def unique(lst):
    if len(lst) == 1:
        return True
    if lst[0] in lst[1:]:
        return False
    
    return unique(lst[1:])
    
    


print(unique([1,2,3,4,5,7,3,6,5,3,8]))
print(unique([1,2,3,4,5,7,6]))
    