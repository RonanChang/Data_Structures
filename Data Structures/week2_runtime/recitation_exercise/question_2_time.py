import timeit
import matplotlib.pyplot as plt
import random

def timeFunction(f,n,repeat=1):
	return timeit.timeit(f.__name__+'('+str(n)+')',setup="from __main__ import "+f.__name__,number=repeat)/repeat

def prefix_average1(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)
    return A

def prefix_average2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0 : j + 1]) / (j + 1)
    return A

def prefix_average3(S):
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j + 1)
    return A

#set the x_values and three y_values as global values
#so they can be used in later functions
x_values = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
prefix_1 = []
prefix_2 = []
prefix_3 = []

def plot_data():

    
    # Your code to draw the plot as shown in the recitation2 file.
    length = len(x_values)
    for i in range(length):
            array = [random.randint(0,1000)] * x_values[i]
            time_1 = timeFunction(prefix_average1,array,repeat=1)           
            prefix_1.append(time_1)
            
            time_2 = timeFunction(prefix_average2,array,repeat=1)           
            prefix_2.append(time_2)
            
            time_3 = timeFunction(prefix_average3,array,repeat=1)
            prefix_3.append(time_3)
        
        
            
            
if __name__ == '__main__':
    plot_data()


line1 = plt.plot(x_values,prefix_1,label = "Linear")
line2 = plt.plot(x_values,prefix_2,label = "Quar")
line3 = plt.plot(x_values,prefix_3,label = "ImpQuar")
plt.xlabel("Input size")
plt.ylabel("Run time")
#plt.legend(handles=[line1,line2,line3])
plt.show()
