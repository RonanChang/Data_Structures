import random

def quick_select(array, k):
    """ Return the kth smallest element of array, for k from 1 to len(array).
        @array: a python list, selecting kth smallest element from it.
        @k:     kth smallest, ranging from 1 to len(array)

        return: value of kth smallest element within array
    """
    # To do
    pass
    

def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))
    print(array)
    k = random.randint(1,20)
    print("Selecting:", k,"th element......")
    print("Your result is:", quick_select(array, k))

    array.sort()
    print("Correct result should be:", array[k - 1])

main()