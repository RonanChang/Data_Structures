#This method is for getting all the possible combinations from a list

import copy
def generateBillboards(names, size, result_list, position):
    if len(result_list) == size:
        print(result_list)
    elif position != len(names):
        copy_list = copy.deepcopy(result_list)
        result_list.append(names[position])
        generateBillboards(names, size, result_list, position + 1)
        generateBillboards(names, size, copy_list, position + 1)
    
    
casts = ["Johnny Depp", "Al Pacino", "Robert De Niro","Kevin Spacey","Denzel Washington", "Russell Crowe","Brad Pitt"]
generateBillboards(casts, 2, [], 0)