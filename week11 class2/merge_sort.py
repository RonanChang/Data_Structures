import random

def merge(temp_array1, temp_array2, array):
    """ Merge two sorted Python lists temp_array1 and temp_array2 into properly sized list S.
        @temp_array1: left half array copy
        @temp_array2: right half array copy
        @array:       the original array being sorted
    """
    # To do
    pass
    

def merge_sort(array):
    """ Sort the elements of Python list using the merge-sort algorithm.
        @array: the original array being sorted
    """
    # To do
    pass

def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    merge_sort(array)
    print("After sorting:")
    print(array)

main()








