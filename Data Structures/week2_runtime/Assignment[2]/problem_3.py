
#The runtime of this function is O(N)
def Search(lst):
    n = len(lst)
    total_of_range = n*(n+1)/2
    total_of_lst = sum(lst)
    missing_num = total_of_range - total_of_lst
    return int(missing_num)

lst = [0,1,3,4,5,6]
print(Search(lst))

    
