import random

def bubble_sort(array):
    ''' Compares each pair of adjacent items and swaps them if they are in the wrong order. 
        @array: the python list being sorted
    '''
    # Your code
    pass


def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    bubble_sort(array)
    print("After sorting:")
    print(array)

main()