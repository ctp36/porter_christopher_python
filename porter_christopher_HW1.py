# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 19:19:52 2016

@author: ctp
"""

# Homework 1
# Math 501
# Chris Porter

#Overall Comment: Very good assignment! You tried to cover all essential situations and commented them well. Since you can
#complete the tasks well, I recommend you to try different methods to figure out which one is more efficient. I have commented
#with "Comment:  " so you may have a look. If any misunderstanding happened, please feel free to email me.

# 1.)
def max(x,y):
    '''
    This function takes two numbers as parameters and returns the maximum value
    
    Parameters:
    x - an integer or decimal value
    y - an integer or decimal value
    
    ctp - Fall 2016
    ''' 
#For the contend between the """, there should be mainly three things, the question, the input parameters, and what kind
#of output do you expect. This will not affect your grade, just friendly reminder.
    var = [x,y]     # initialize the list var
    for num in var: # this for loop checks that each variable in var is a 
                    # number and asks the user to change variables if not.
        if num.__class__ not in [int, float, complex]:    
            return "Please change '" + str(num) + "' to a number"
        
        
        
    if x > y:     # If x is greater than y it is the larger of the two values
        return x    # And therefore the maximum, so return x.           
        
    else:           # y is greater than or equal to y, making y the maximum 
        return y    # value, so return y.

#Comment: For the function name, try to not conflict with the default function of python. How about the x==y situation output?
# You should add examples for your functions.

# 2.)
def max_of_three(x,y,z):    
    '''
    This function takes 3 numbers as parameters 
    and returns the largest value of the three
    
    parameters:
    x - an integer or decimal value
    y - an integer or decimal value
    z - an integer or decimal value
    
    ctp - Fall 2016
    '''    
    var = [x,y,z]   # initialize the list var
    for num in var: # this for loop checks that each variable in var is a 
                    # number and asks the user to change variables if not.
        if num.__class__ not in [int, float, complex]:    
            return "Please change '" + str(num) + "' to a number"
    
    if (x > y) and (x > z):  # This Checks if x is larger than both y and z
        return x
    
    elif (y > x) and (y > z): # This Checks if y is larger than both x and z        
        return y
    
    elif (z > x) and (z > y): # This Checks if z is larger than both y and x       
        return z

        
        
# 3.)
def stringorlist_length(stringorlist):
    '''
    This Function computes the length of a given string or list by
    looping over each character or element in a list or string
    Counting each character or element iteratively
    
    Parameter:
    stringorlist - this is either a list or string.
    
    ctp - Fall 2016
    '''
    if stringorlist.__class__ not in [list, str]:
        return "Please input a list or string for this function"
        
    
    a = 0                 # Initialize the variable which will store the length
    for element in stringorlist: # loop over the string or list
        a += 1           # add 1 to our return variable which stores the length        
            
    return a
#Comment: Actually, you can use 'i' to substitute the 'element' you used here.


# 4.)
def thevowels(char):
    ''' 
    This function checks if a character is a vowel.
    It creates a string variable containing upper and lowercase vowels
    Then checks whether the character is in that string
    
    Parameter:
    char - a single character, string of length 1
    
    ctp - Fall 2016
    '''
    
    # Two If statements to check that the input is a string of length 1
    if char.__class__ != str:
        return "Please input a string of length 1"

    if len(char) != 1:
        return "Please input a string of length 1"    
    
    vowel = 'aeiouAEIOU' # This is our vowel string with both upper and lower 
                         # case vowels
    if char in vowel:    # Checks if the character is in our vowel string    
        return True      # If our character parameter is a vowel we return true  
    
    return False         # If our character parameter is not a vowel, return 
                         # False
#Comment: use the loop as "if...else..."

# 5.)
def translate(stringy):
    ''''
    This function's purpose is to take a string and convert it to "Robber's 
    Language, which is a language where a word or sentence is turned into a
    word where consonants are duplicated and an "o" is placed between them, 
    spaces are removed, and vowels are left alone.
    
    Parameters:
    stringy -  a string containing a word, phrase
    
    ctp - Fall 2016
    '''
    # Check that the input is a string.    
    if stringy.__class__ != str:
        return "Please change the input to a string"
        
    vowels = 'aeiouAEIOU' # create a variable to determine vowels
    newstringy = ''       # Initialize our return variable 
    for letter in stringy:  # loop over each character in the string
        if letter == " ":   # If the character is a space, skip over this using
                            # continue
           continue     
        else:
            newstringy  += letter.lower()    # Append each character to our return value
            if letter not in vowels:  # Check for consonants
                newstringy = newstringy + 'o' + letter.lower() # When consonant
                                                               # also append a 
                                                               # "o" and the
                                                             # character again.
            
    return newstringy



# 6.)
def sum(numlist):
    '''
    This function sums all the values in our parameter list.
    
    Parameters:
    numlist - a list containing values
    
    ctp - Fall 2016
    '''
    if numlist.__class__ != list: # Check that the input is a list
        return "Please input a List"
    
    for num in numlist:           # Check that each element in list is a number
        if num.__class__ not in [int, float, complex]:
            return "Please replace '" + str(num) + "'  with a number."
            
    sum = 0             # Initialize our return variable "sum"
    for val in numlist: # loop over the values in our parameter
        sum += val      # add each value to the sum as we loop through the list
    
    return sum



def multiply(numlist):
    '''
    This function multiplies all the values in our parameter list.
    
    Parameters:
    numlist - a list containing values
    '''
    if numlist.__class__ != list: # Check that the input is a list
        return "Please input a List"
    
    for num in numlist:           # Check that each element in list is a number
        if num.__class__ not in [int, float, complex]:
            return "Please replace '" + str(num) + "'  with a number."
            
            
    multiply = 1        # Initialize our return variable "sum"
    for val in numlist: # loop over the values in our parameter
        multiply *= val # add each value to the sum as we loop through the list
    
    return multiply



# 7.)
def reverse(stringy):
    '''
    This function takes in a string and returns the reverse of that string 
    Removing any space characters
    
    It does this by converting it to a list, and insert each letter to the 
    beginning of the list, then convert it back to a string
    
    Parameter:
    stringy -  a string containing a word or phrase
    
    ctp - Fall 2016
    '''
    if stringy.__class__ != str:        # Check that the input is a string.
        return "Please input a string"
        
    reverse = []               # Initialize our list of reversed characters
    listy = list(stringy)      # create a list from our string parameter

    for letter in listy:      # loop over each element in the list we just made
        if letter == " ":     # Skip over blanks
            continue        
        reverse.insert(0,letter)  # insert each iterative character to 
                                  # beginning of the reverse list
    return ''.join(reverse)       # conver the list back to a string and return
    


# 8.)
def is_palindrome(word):
    '''
    This function checks to see if a word is a palindrome.
    Meaning it is the same forwards as it is backwards.
    
    Parameters:
    word - a word in the form of a string
    
    ctp - Fall 2016
    '''
    
    if word.__class__ != str:
        return "Please input a string instead"
    
    # This functin has two parts, the first of which is to reverse the word
    # that is the input to the function.   
    
    word = word.lower()        # Set all letters to lower case
    reverse = []               # Initialize our list of reversed characters
    listy = list(word)         # create a list from our string parameter

    for letter in listy:      # loop over each element in the list we just made
        if letter == " ":     # Skip over blanks
            continue        
        reverse.insert(0,letter) # insert each iterative character to 
                                 # beginning of the reverse list
    reverse =  ''.join(reverse)  # convert the list back to a string and return
    
    # The second part of the function is to check if the reversed form of the
    # word is the same as the input.
    
    return reverse == word.replace(' ','')



# 9.)
def is_member(x,a):
    '''
    This function take a value (x) and checks if it is in a list of values (a)
    
    It does this by looping over a, checking if x is equal to any value in a.
    
    Parameters:
    x - a value of a number, sting, etc.
    a - a list of values 
    
    ctp - Fall 2016
    '''
    # Two if statements to check each input variable is as expected.
    if len(x) != 1:
        return "Please input a single value for the first argument"
    if a.__class__ != list:
        return  "Please change second argument to a list."
        
    for val in a:       # Loop through the list a
        if x == val:    # check if parameter x is in a, return true if 
            return True # x is equal to val
            
    return False        # Return false when x is not equal to any value in a.
    
    
    
# 10.)
def overlapping(list_a, list_b):
    '''
    This  function takes two lists, and determines if they have any elements 
    in common.
    
    If it finds two identical elements in the lists it will return a True.
    Otherwise a False.
    
    Parameters:
    list_a - a list, to be checked against our other parameter
    list_b - a list, to be checked against our other parameter
    
    ctp - Fall 2016
    '''
    listlist = [list_a, list_b] # Initialize a list variable with our inputs
                                # as it's two elements.
    
    # This loop checks that our inputs are both lists.
    for listy in listlist:
        if listy.__class__ != list:
            return "Please change your inputs to two lists"
            
    for val_a in list_a:            # loop through list a
        for val_b in list_b:        # loop through list b
            if val_a == val_b:      # compare each element in a with each
                                    # element in b
                return True         # When this is True return True
                
    return False                    # If the loop completes and finds no match
                                    # return False
    


# 11.)
def generate_n_chars(n,c):
    '''
    This function takes in an integer n and a character c, and returns
    a string n characters long consisting of the character c.
    
    Parameter:
    n - an integer, determines the length of the returned string
    c - a character, determines the charact of the returned string
    
    ctp - Fall 2016
    '''
    
    if n.__class__ != int:
        return "Change '" + n + "' to a integer"
    if c.__class__ not in [str, int]:
        return "Change '" + c + "'to a string or integer of length one"
    
    if isinstance(c,str) is False: # First check if c is a string
        c = str(c)                 # If it is not, convert it to a string
    
    if len(c) != 1:
        return "Change '" + str(c) + "' to a string or integer of length one"
        
    stringy = ""                   # Initialize the return string
    for val in range(n):           # loop through a range from 0 to n-1
        stringy += c               # append c to stringy
        
    return stringy        
    


# 12.)
def histogram(intList):
    '''
    This function takes a list of integers and returns a histogram composed 
    of those integers.
    
    The histogram is visualized as strings of * delimited by " ".
    
    Parameter:
    
    intList - a list composed of integers.
    
    ctp - Fall 2016
    '''
    if intList.__class__ != list:
        return "Please input a list"
    
    for num in intList:
        if num.__class__ != int:
            return "Please change '" + str(num) + "' to an integer"
        
    histString = ""
    
    for integ in intList:
        for n in range(integ):
            histString += '*'
        
        histString += ' '
    
    return histString



# 13.)
def max_in_list(numList):
    '''
    This function takes in a list of numbers and returns the largest value in 
    the list
    
    Parameters:
    numList - a list containing numbers
    
    ctp - Fall 2016
    '''
    if numList.__class__ != list:       # check that the input is a list
        return "Please input to a list."
    else:                               
        for num in numList:             # Check each element in the list
            if num.__class__ not in [int, float, complex]: # check it's a number
                return "Please change '" + str(num) + "' to a number."
            
            
    max = numList[0]        # initialize the return value max as the first
                            # value of numList
    for val in numList:     # loop through the values in numList
        if max > val:       # check if max is greater than val
            continue        # If true continue through the loop
        else:               # If val is greater than max
            max = val       # Set max equal to val
    
    return max
    


# 14.)
def words_to_integers(wordList):
    '''
    This function takes in a list consisting of words and returns
    a list composed of numbers corresponding to the length of eachs word
    
    Parameters:
    wordList - a list composed of words
    
    ctp Fall 2016
    '''
    # check that the input is a list.
    if wordList.__class__ != list:
        return "Input must be a list."
    
    # check that each element is a string.
    for word in wordList:
        if word.__class__ != str:
            return "Please change '" + str(word) + "' to a word."
            
    intList = []            # initialize list of integers to return
    
    for word in wordList:       # Loop through the list of words
        val = 0                     # initialize a variable to append to the list    
        for letter in word:         # loop through each letter in word
            val += 1                    # count each letter in word
            
        intList.append(val)         # append the length of each word to the
                                    # intList return variable
    
    return intList



# 15.)
def find_longest_word(wordList):
    '''
    This function takes in a list of words and returns the length of the 
    longest word
    
    It does this in two steps. First, determine the length of each word. Second
    determine the max length
    
    Parameter:
    wordList -a list where each element is a word.
    
    ctp - Fall 2016
    '''
    # check that the input is a list.
    if wordList.__class__ != list:
        return "Input must be a list."
    
    # check that each element is a string.
    for word in wordList:
        if word.__class__ != str:
            return "Please change '" + str(word) + "' to a word."    
    
    intList = []            # initialize list of integers to return
    
    for word in wordList:       # Loop through the list of words
        val = 0                     # initialize a variable to append to the list    
        for letter in word:         # loop through each letter in word
            val += 1                    # count each letter in word
            
        intList.append(val)         # append the length of each word to the
                                    # intList return variable
        
    max = intList[0]        # initialize a maximum value as the first value in
                            # the List of integers returned in step 1
    
    for integ in intList:       # Loop throug the values in intList
        if max > integ:             # check if max is greater than val
            continue                # If true continue through the loop
        
        else:                       # If integ is greater than the max value
            max = integ             # set max to the integer value
            
    return max
    


# 16.)
def filter_long_words(wordsList,n):
    '''
    This function takes in a list of words and a a value n. It returns a list 
    of words that are in the input list and have a length greater than n
    
    It does this in two steps. First, determine the length of each word. 
    Second, remove each word that is not greater than n
    
    
    Parameter:
    wordList -a list where each element is a word.
    
    ctp - Fall 2016
    '''
    # check that the first argument is a list.
    if wordsList.__class__ != list:
        return "Input must be a list."
    
    # check that each element in the first argument is a string.
    for word in wordsList:
        if word.__class__ != str:
            return "Please change '" + str(word) + "' to a word."    
    
    # Check that the second argument is a number.
    if n != int:
        return "Please input an integer."
    
    returnList = wordsList  # intiliaze to return, as lists are mutable
    
    for word in wordsList:       # Loop through the list of words
        val = 0                     # initialize a variable to append to the list    
        for letter in word:         # loop through each letter in word
            val += 1                    # count each letter in word
        
        if val > n:              # Check that the length of each word is greater
            continue             # than n. If it is continue the loop, otherwise
                                 # process the next two lines.
        index = returnList.index(word)     # get the first location in returnList
                                           # of 'word'.    
        returnList.pop(index)    # Remove that word from the list using pop.
    
    return returnList

