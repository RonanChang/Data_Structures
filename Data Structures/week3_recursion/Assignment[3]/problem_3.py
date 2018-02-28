#The first method is provided, a recursive function

def recur(n):
    if (n < 0):
        return -1
    elif (n < 10):
        return 1
    else:
        return (1 + recur(n // 10))
    
print(recur(1000))


#This is the method using iteration as required

def recur_iteration(n):
    result = 0

    if n < 0:
        return -1
  
    while n > 0:
        result += 1
        n = n //10
            
    return result
    
print(recur_iteration(1000))
