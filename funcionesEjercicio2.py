import string

from collections import Counter
def most_frequent(List):
    count = Counter(List)
    return count.most_common(1)#[0][0]

#def is_word(chain):
#    if not string.ascii_letters in chain:
#        return False
#    else:
#        return True

def remove_not_words(List):
    res = [i for i in List if i.isalpha()]
    return res

#Sacado de StackOverflow
#str.isalpha() is only true if all characters in the string are letters: Return true if all characters in the string are alphabetic and there is at least one character, false otherwise.