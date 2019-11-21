# Author: Brian Hoang
# Date: 11/20/2019
# Description: function that takes two strings as parameters and creates a
# set for words that exist in both strings

#takes in two strings as parameters
def words_in_both(firstring,secstring):
    #makes all strigns lowercase
    firstring = firstring.lower()
    secstring = secstring.lower()
    #creates a list of each word in each string
    firstring_list = firstring.split()
    secstring_list = secstring.split()
    #creates set called bothset
    bothset = set()
    tally = 0
    #for loop that checks for similar words and adds those similar words to bothset
    for tally in range(len(firstring_list)):
        if firstring_list[tally] in secstring_list:
            bothset.add(firstring_list[tally])
            tally += 1
        elif firstring_list[tally] not in secstring_list:
                tally += 1
    return bothset

#string1 = "My dog is sick"
#string2 = "How sick is your dog"
#print(words_in_both(string1,string2))
