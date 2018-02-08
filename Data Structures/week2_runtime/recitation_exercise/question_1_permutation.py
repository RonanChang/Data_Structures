import timeit
import random



def permutation1(array):
    # Your code to implement permutation 1
    n = len(array)

    for i in range(n):
        num = random.randint(0,n-1)
        if num not in array:
            array[i] = num

    return array
            
        

    
def permutation2(array):
    # Your code to implement permutation 2
    n = len(array)
    used = [False] * n
    
    for i in range(n):
        num = random.randint(0,n-1)
        while used[num] == True:
            num = random.randint(0,n-1)
        if used[num] == False:
            array[i] = num
            used[num] = True
                  
    return array
    
      

    
def permutation3(array):
    # Your code to implement permutation 3
    n = len(array)
    for i in range(n):
        array[i] = i
    
    for i in range(n):
        index = random.randint(0,i)
        current = array[i]
        array[i] = array[index]
        array[index] = current
        
    return array
        

print(permutation1([0,1,2,3,4]))
print(permutation2([0,1,2,3,4]))
print(permutation3([0,1,2,3,4]))
        
