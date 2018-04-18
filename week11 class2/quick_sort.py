import random

def medianOfThree(array, start, end):
    ''' Determines the median of three values in a portion of the array. 
        Considers three values in the portion: first, last and middle position.
        This function sorts those three positions, then return the middle value.
        @array: the list being sorted
        @start: the index of first element in this portion
        @end: the index of last element in this portion

        return: middle value
    '''
    # To do
    pass


def partition(array, start, end, pivot_value):
    ''' partitions a portion of the array around a pivot value. 
        @array: the list being sorted
        @start: the index of first element in this portion
        @end :  the index of last element in this portion
        @pivot_value: the pivot value for the partition

        return: index of pivot_value after partition
    '''
    # To do
    pass

def quick_sort(array, start, end):
    ''' Performs quick sort on a portion of the array. 
        Use start, end to perform recursion.
        @array: the list being sorted
        @start: the index of first element in this portion
        @end :  the index of last element in this portion
    '''
    # To do
    pass


def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    quick_sort(array, 0, len(array) - 1)
    print("After sorting:")
    print(array)

main()












