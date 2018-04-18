Student Name: Ruonan Chang
NetId: rc3477

=============================================================
Problem_1:

'''
The runtime of this function is O(logN)
'''
=============================================================
Problem_2:
#this method can handle both negative and positive exponents

def Power(x,n):
    if n == 0:
        return 1
    elif n > 0:
        return x * Power(x,n-1)
    else:
        return 1/x * Power(x,n+1)
    

print(Power(2,-4))
print(Power(3,4))

=============================================================
Problem_3:
#This is the recursive function provided:
def recur(n):
    if (n < 0):
        return -1
    elif (n < 10):
        return 1
    else:
        return (1 + recur(n // 10))
    
print(recur(10))

#This is the method using iteration as required:
def recur_iteration(n):
    result = 0

    if n < 0:
        return -1
  
    while n > 0:
        result += 1
        n = n //10
            
    return result
    
print(recur_iteration(1000))

===============================================================
Problem_4:
#The runtime of this function is O(n^2)
def unique(lst):
    if len(lst) == 1:
        return True
    if lst[0] in lst[1:]:
        return False
    
    return unique(lst[1:])
    

print(unique([1,2,3,4,5,7,3,6,5,3,8]))
print(unique([1,2,3,4,5,7,6]))

================================================================
Problem_5:
#This is the method of drawing Pascal triangle using recursion:

def Pascal_recursive(n):

   #if n = 1, only add "1"
   #if n > 1, add sum = prev_list[n-1] + list[n-2]
   #recur(n - 1)
   if n == 1:
       row = [[1]]
       return row
   else:
       row = [1]
       rows = Pascal_recursive(n - 1)
       prev_row = rows[-1]
       
       for i in range(len(prev_row) - 1):
           row.append(prev_row[i] + prev_row[i+1])
       row.append(1)
       rows.append(row)
   return rows


def main():
    Pascal = Pascal_recursive(5)
    N = len(Pascal)
 
    for n in range(N):
        each_row = Pascal[n]
        m = len(each_row)
        for i in range(m):
            new_item = str(each_row[i])
            each_row[i] = new_item
        
        print(" " * ((N - m)) ," ".join(each_row))
             

main()
    
=================================================================
Problem_6:
#get all possible combinations from a list:

import copy
def generateBillboards(names, size, result_list, position):
    if len(result_list) == size:
        print(result_list)
    elif position != len(names):
        copy_list = copy.deepcopy(result_list)
        result_list.append(names[position])
        generateBillboards(names, size, result_list, position + 1)
        generateBillboards(names, size, copy_list, position + 1)
    
    
casts = ["Johnny Depp", "Al Pacino", "Robert De Niro","Kevin Spacey","Denzel Washington", "Russell Crowe","Brad Pitt"]
generateBillboards(casts, 2, [], 0)