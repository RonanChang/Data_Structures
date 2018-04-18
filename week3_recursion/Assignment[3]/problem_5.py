#This is the method of drawing Pascal triangle in recursion

def Pascal_recursive(n):

   #if n = 1, only add "1"
   #if n > 1, add sum = prev_list[n-1] + list[n-2]
   #recur(n - 1)
   if n == 1:
       row = [[1]]
       return row
   else:
       row = [1]
       rows = Pascal_recursive(n - 1)
       prev_row = rows[-1]
       
       for i in range(len(prev_row) - 1):
           row.append(prev_row[i] + prev_row[i+1])
       row.append(1)
       rows.append(row)
   return rows


def main():
    Pascal = Pascal_recursive(5)
    N = len(Pascal)
 
    for n in range(N):
        each_row = Pascal[n]
        m = len(each_row)
        for i in range(m):
            new_item = str(each_row[i])
            each_row[i] = new_item
        
        print(" " * ((N - m)) ," ".join(each_row))
             

main()
    
    
           
    
    
        
    