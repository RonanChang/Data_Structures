import ctypes


class UserDefinedDynamicArray:
    def __init__(self,I=None):
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)
        if I:
            self.extend(I)

    def __len__(self):
        return self._n

    def append(self,x):
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n]=x
        self._n+=1

    def _resize(self,newsize):
        A=self._make_array(newsize)
        self._capacity=newsize
        for i in range(self._n):
            A[i]=self._A[i]
        self._A=A

    def _make_array(self,size):
        return (size*ctypes.py_object)()

    def __getitem__(self,i):
        if isinstance(i,slice):
            A=UserDefinedDynamicArray()
            for j in range(*i.indices(self._n)): # * operator was used to unpack the slice tuple
                A.append(self._A[j])
            return A
        if i<0:
            i=self._n+i
        return self._A[i]

    def __delitem__(self,i):
        if isinstance(i,slice):
            #A=UserDefinedDynamicArray()
            for j in reversed(range(*i.indices(self._n))):
                 del self[j]
        else:
            if i<0:
                i=self._n+i
            for j in range(i,self._n-1):
                self._A[j]=self._A[j+1]
            self[-1]=None        
            self._n-=1


    def __str__(self):
        return "[" \
               +"".join( str(i)+"," for i in self[:-1]) \
               +(str(self[-1]) if not self.is_empty() else "") \
               +"]"

    def is_empty(self):
        # we will do in class
        # return true if array is empty otherwise false
        # Your Code
        if self.__len__() == 0:
            return True
        else:
            return False
        

    def __iter__(self):
        # we will do in class, iterate through the list using yield
        # Your Code
        for i in range(self.__len__()):
            yield self._A[i]
                   

    def __setitem__(self,i,x):
        #we will do in class, think about how to handle negative index
        # Your code
        if i < 0:
            i = self.__len__() + i
        self._A[i] = x
        


    def extend(self,I):
        # append all elements of I to the self
        for i in I:
            self.append(i)
        
    def reverse(self):
        #we will do in class
        # reverse the list
        # your code
        for i in range(self.__len__() // 2):
            j = self.__len__() - i
            self._A[i],self._A[j] = self._A[j],self._A[i]
    

    def __contains__(self,x):
        #we will do in class
        # If element x is present in the list return true otherwise false
        # your code
        for each in self:
            if each == x:
                return True
            return False

    def index(self,x):
        #we will do in class
        # Return the index of first occurrence of element x, if not found in the list return None.
        # Your code
        for i in range(self.__len__()):
            if self._A[i] == x:
                return i
        return None

    def count(self,x):
        #we will do in class
        # return how many times element x is present in the list
        # Your code
        count = 0
        for i in self:
            if i == x:
                count += 1
        return count

    def __add__(self,other):
        # we will do in class
        # '+' Operator Overloading for UserDefinedDyamicArray Class like myList1+myList2 will return a list containing all the elements of myList1 and then myList2
        # Your code
        array = UserDefinedDynamicArray(self)
        array.extend(other)
        return array
        

    def __mul__(self,times):
        # we will do in class
        # '*' Operator Overloading for UserDefinedDyamicArray Class like myList1*3 will return a list having myList1 elements three times.
        # Your code
        array = UserDefinedDynamicArray(self)
        for i in range(times):       
            array.extend(self)

    __rmul__=__mul__



    def pop(self,i=-1):
        # We will do in class
        # delete element at position i using del keyword, by default we delete the last element from UserDefinedDyamicArray and return the element to the calling method
        # Your Code
        if i < 0:
            i = self._len_() + i
        to_return = self[i]
        del self[i]
        return to_return
        
        
    def remove(self,x):
        #we will do in class
        # remove element x from the list, we will delete the first occurrence of element x from the list
        # at first find out the index of element x, then delete it
        del self[self.index(x)]
    
    def max(self):
        # Task 9
        # Return the max element in self._A
        pass

    def min(self):
        # Task 9
        # Return the min element in self._A
        pass

    def sort(self, order = "asc"):
    	# Task 10
    	# Sort self._A in ascending order if order == "asc"
    	# otherwise sort in descending order if order = 'desc'
    	# if order parameter value is wrong, do nothing.
    	pass


def main():
#### Task1: Print the lists
####  create two empty list myList1 and myList2, append some elements and print it. You need to implement __len__ and __iter__ methods in the UserDefinedDyanmicArray class.
    myList1 = UserDefinedDynamicArray()
    print("myList1: ",myList1)
    myList1.append(3)
    print("myList1 after appending 3: ",myList1)

    myList2=UserDefinedDynamicArray()
    for i in range(10):
        myList2.append((i+1)*20)
    print("myList2: ",myList2)

####  Task2: Delete elements from the myList2 using "del" keyword. __delitem__ method is already given but you need to write __setitem__ method to make it run.
####  suppose we want to delete 2nd, third, and four elements from myList2 by as follows. This will give you an error as __setitem__ method needs to be complete

    del myList2[2:5]
    print("myList2 after deleting: ",myList2)

    
####  Task3: extending the list using extend function and creating a list from an existing list
####  suppose we want to use extend myList1 by adding all the elements in myList2 by calling the extend(self, I) function in the UserDefinedDynamicArray Class

    myList1.extend(myList2)
    print("myList1 after extending: ",myList1)

####  Task4: Reverse a list by calling myList2.reverse(), it will reverse the list.
    myList2.reverse()
    print("myList2 after reversing: ",myList2)

####  Task5: Implement __contains__(self,x), count(x), and index(x) as described in the UserDefinedDynamicArray class.
####  __contains__ will check whether element x is present in the list. If yes return true, otherwise false
####  index(x) will return the index of element x in the list. If x is present multiple times, it will return the first index of x, otherwise it will return None
####  count(x) will return how many times element x is present in the list. If the element x is not present, it will return 0.
    x=140
    print("Whether x is present in the myList1: ",x in myList1) #contains function check
    print("x current position in the myList1 is ",myList1.index(x))
    print("Number of times x appears in the myList1 is ",myList1.count(x))



####  Task6: Implement __add__(self,other) and __mul__(self,times) as described in the UserDefinedDynamicArray class.
####  __add__ will implement '+' Operator Overloading for UserDefinedDyamicArray Class
####  like myList1+myList2 will return a list containing all the elements of myList1 and then myList2
####  --mul__ qill implement '*' Operator Overloading for UserDefinedDyamicArray Class like myList1*3 will return a list having myList1 elements three times.
    myList3=myList1+myList2
    print("myList3 after adding : ",myList3)
    myList4 = 2*myList1
    print("myList4 after multiplying : ",myList4)
    


####   Task7: Implement pop(i) function for UserDefinedDynamicArray Class. Implement remove method for UserDefinedDynamicArray Class.
####   By default pop will return the last element from the list and delete that element from the list using del keyword.
####   if i value is specified then we will delete the element at position i and return it to the calling method.
####   remove(x) will delete the element x from the list. If x is present multiple time, it will delete the first occurrence of x.

    p=myList2.pop(1)
    print("Popped element at position 1 from myList2 ",p)
    myList1.remove(140)
    print("myList1 after removing: ",myList1)

    
####   Task8: Modify __delitem__(self,i) function for UserDefinedDynamicArray Class.
####   Current __delitem__(self, i) function does not shrink the array capacity. 
####   We want to shrink the array capacity by half if total number of actual elements reduces to one fourth of the capacity.
    print("--------------------Task 8--------------------")

    print(myList2, "capacity:", myList2._capacity)
    for i in range(7):
        del myList2[0]
    print(myList2, "capacity:", myList2._capacity)
        
####   Task9: Implement max(self); min(self) functions for UserDefinedDynamicArray Class.
####   max(self) function which return maximum element among the elements of self._A.
####   min(self) function which will return minimum element among the elements of self._A.
    print("--------------------Task 9--------------------")

    print("Max of list: ", myList2.max())
    print("Min of List: ", myList2.min())


####   Task10: Implement sort(self, order='asc')
####   sort function which will sort the list by default ascending order
####   otherwise descending order if order = 'desc'
    print("--------------------Task 10--------------------")

    myList2.sort()
    print("After ascending sort: ", myList2)
    myList2.sort(order = 'desc')
    print("After descending sort: ", myList2)

    
if __name__ == '__main__':
    main()
