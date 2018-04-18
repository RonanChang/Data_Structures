
def palindrome(param):
    #find the middle index
    #make sure the left side == right side
    #no matter the length is odd or even number,
    #we always check from the (middle - 1)
    index = (len(param) - (len(param) % 2)) // 2 - 1
    
    for i in range(index):        
        #notice! we wanna check if param[0] == param[-1]
        if param[index] != param[-index - 1]:
            return False
        else:
            return True

test = palindrome("ddddfdddd")
test2 = palindrome("dfsgsh")
print(test,test2)

