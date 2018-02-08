
#ignore all the white space and punctuation
ignore = ['.', ' ', ',', ';', ':', '?', '!'] 


def anagram(param1,param2):
    #check whether all the characters in param1 is in param2
    #the number of each charatcer should be the same
    for character in param1:
        if character not in ignore and param1.count(character) != param2.count(character):
            return False

    #check it again for param2
    for character in param2:
        if character not in ignore and param1.count(character) != param2.count(character):
             return False

    return True

state = anagram("sso","so")
state2 = anagram("otto","toot")
state3 = anagram("ron an","rofred,nan")

print('anagram("sso","so") == ' + str(state))
print('anagram("otto","toot") == ' + str(state2))
print('anagram("ron an","rofred,nan") == ' + str(state3))
            
        
