
def add_one(num_list):
    #convert the string to a list and convert the list into an int
    #int + 1
    new_num = int(''.join(str(x) for x in num_list)) + 1

    #convert the new int back to str
    #and then convert the new string to a new list
    new_list = [int(x) for x in str(new_num)]
    return new_list

test = add_one([9,9,9])
print(test)
