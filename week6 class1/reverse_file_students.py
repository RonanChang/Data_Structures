from array_stack_Students import ArrayStack

def reverse_file(filename):
  """Overwrite given file with its contents line-by-line reversed."""

  inputfile = open(filename,'r')
  
  # to do
  my_stack = ArrayStack()
  line = inputfile.readline()
  while line != '':
      my_stack.push(line.rstrip())
      line = inputfile.readline()
      
  inputfile.close()
  # now we overwrite with contents in LIFO order
  output = open(filename, 'w')    # reopening file overwrites original
   
  # to do
  while not my_stack.is_empty():
      new_line = my_stack.pop()
      output.write(new_line + "\n")  #don't forget to change line 
  output.close()

reverse_file('DSSyllabus.txt')
