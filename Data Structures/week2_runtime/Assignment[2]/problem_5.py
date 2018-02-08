
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
