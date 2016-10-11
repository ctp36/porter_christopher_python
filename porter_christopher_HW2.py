# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:11:41 2016

@author: chris_000
"""

# Homework 2 
# Math 510
# Chris Porter

#Overall comment: Very good exercise and explanations. You have commented all your thoughts in detail and the logic is very
#                 clear which is good for your future review. But I suggest you to simplify your logic or improve efficiency
#                 with advanced functions.

# 1.)
def palindrome_reader(file):
    '''
    This function reads a file submitted by the user, and checks if each line
    is a palindrome.  For each line in the file, if it is palindrome the line
    is printed to the screen.
    
    First, define a function named is_palindrome that checks if a string is 
    palindrome.
    
    Then define a function which reads a file, loops through each line,
    uses is_palindrome to check each line, and returns a print out of each
    palindrome in the file.
    
    Parameters:
    file - a file containing lines of texts
    
    ctp - Fall 2016 
    '''
    
    
    def is_palindrome(word):
        '''
        This function checks to see if a word is a palindrome.
        Meaning it is the same forwards as it is backwards.
    
        Parameters:
        word - a word in the form of a string
    
        ctp - Fall 2016
        '''           
    
        # This functin has two parts, the first of which is to reverse the word
        # that is the input to the function.   
    
        word = word.lower()        # Set all letters to lower case
        
        reverse = []              # Initialize our list of reversed characters
        listy = list(word)        # create a list from our string parameter
        
        for letter in listy:      # loop over each element in the list we just made
            if letter == " ":     # Skip over blanks
                continue        
            reverse.insert(0,letter) # insert each iterative character to 
                                     # beginning of the reverse list
        reverse =  ''.join(reverse)  # convert the list back to a string and 
                                     # return
    
        # The second part of the function is to check if the reversed form of the
        # word is the same as the input.
    
        return reverse == word.replace(' ','')   # return a boolean
 

    filereader = open(file) # read the user input file
    
    for line in filereader:        # loop through each line
        line = line.rstrip()       # rstrip the end of the line 
        
        if is_palindrome(line):     # Use is_palindrome to check if the line is
            print(line)             # a palindrome and print it to screen.
    
    filereader.close() # close the file
        
#Comment: This method do work. Since you can complete this task, I suggest you to find an more efficient method to figure
#         this out. For example to combine those two parts into one function.


# 2.)
def semordnilap(file):
    '''
    A semordnilap is a word or phrase that spells a different word or phrase 
    backwards. ("Semordnilap" is itself "palindromes" spelled backwards.) 
    
    This function contains a semordnilap recogniser that accepts a file name 
    (pointing to a list  of words) from the user and finds and prints all pairs
    of words that are semordnilaps to the screen. 
    
    For example, if "stressed" and "desserts" is part of the word list, the the
    output should include the pair "stressed desserts".
    
    Parameters:
    file - a file that contains a list of words, which will be searched for 
    'semordnilaps'
    
    ctp  - Fall 2016
    '''
    
    
    def semordnilap_si(word_a, word_b):
        '''
        This function checks to see if a pair of words are a semordnilap.
        Meaning the two words are mirror images of each other.
    
        Parameters:
        word_a - a word in the form of a string
        word_b - a word in the form of a string    
        
        ctp - Fall 2016
        '''           
    
        # This functin has two parts, the first of which is to reverse the word
        # that is the input to the function.   
    
        word = word_a.lower()        # Set all letters to lower case
        
        reverse = []              # Initialize our list of reversed characters
        listy = list(word)        # create a list from our string parameter
        
        for letter in listy:      # loop over each element in the list we just made
            if letter == " ":     # Skip over blanks
                continue        
            reverse.insert(0,letter) # insert each iterative character to 
                                     # beginning of the reverse list
        reverse =  ''.join(reverse)  # convert the list back to a string and 
                                     # return
    
        # The second part of the function is to check if the reversed form of the
        # word is the same as the input.
    
        return reverse == word_b.replace(' ','')   # return a boolean
    
    filereader = open(file) # read the user input file
    
    wordlist = []       # initialize a list of words in the file
    returnList = []     # initialize a list of semordnilaps
    
    for word in filereader:      # loop through each word in the file
        word = word.rstrip()     # strip out any whitespace 
        wordlist.append(word)    # append each word to a list
    
    filereader.close()   # close the file
     
    for word_a in wordlist:      # loop through the list of words as word_a
        for word_b in wordlist:  # a second loop, used to compare to the word in the first loop. 
            if semordnilap_si(word_a, word_b):    # Check if the words are semordnilaps
                pair = str(word_a) + " " + str(word_b) # create the semordnilap pair                
                reversePair = str(word_b) + " " + str(word_a)   # create the reverse of the pair
                if reversePair in returnList:                   # check to see if the reverse 
                                                                # is already in the list
                    pass                                        # if so, don't append
                else:                  # if the pair is not in the list
                    returnList.append(pair)                # append the pair to the return list
                  
    
    print(returnList)     # print the list of semrdnilaps
#Comment: Still, you method works but maybe you have defined so many words to make the logic very complicated so that it take
#         a while to follow it. You can try to simplify your logic or improve the efficiency with advanced functions.

# 3.)
def char_freq_table(file):
    '''
    This function accepts a filename from the user, 
    and builds a frequency listing of the characters
    in the file.  It then prints a sorted and 
    nicely formatted character frequency table to
    the screen.
    
    It does this in 5 stepts. The first step is to read in 
    the file and initialize two lists used to quantify the 
    characters in the file.
    
    The second step is to structure the data used to calculate
    the number of times a character is in list.
    
    The third step is to aggregate the data. The fourth step 
    is to format the data for printing. Then finally print the data
    
    Parameter:
    file - a string that represents the filename and extension
    of the file the function will read and summarize by character.
    
    ctp -Fall 2016
    '''
    
    from operator import itemgetter     # itemgetter from operator module used to sort a tuple
    
    fileReader = open(file)             # read the file
    
    lineList = []                       # initialize a list, consisting of the lines in file
    letterList = []                     # initialize a list, consisting of the letters in file
    
    for line in fileReader:             # loop over the lines in file
        lineList.append(line.strip())   # create a list consisting of each line in file
        
    fileReader.close()                  # close file
    
    for line in lineList:               # loop over the each string in lineList
        for letter in line:             # loop over each letter/character in the string 
            letterList.append(letter)   # create a list consisting of each letter/character in the list
    
    letterDict = dict.fromkeys(letterList)  # create a dictionary consisting of each unique character in letterList
    
    for key in letterDict:                  # loop over each key value (character) in letterDict
        letterDict[key] = letterList.count(key) # Update the value in ltterDict to the count of each letter in letterList
   
    sortedLetterFreq = sorted(letterDict.items(), key=itemgetter(1), reverse=True)  # sort the dictionary by 
                                                                                    # copying it to sorted tuple
                                                                                    # sorted off the value
                                                                                    # in descending order
    
    for (x,y) in sortedLetterFreq:          # loop over the tuple, and print each 
        print(x, y)                         # letter, count combo in descending order.
        
        
# 4.)
def speak_ICAO(file, letter_pause, word_pause):
    '''
    This function translates a text to the ICAO alphabet and reads back the alphabet
    letter by letter in the ICAO alphabet.  
    
    Parameters:
    file - a file of text to be read and translated.
    letter_pause - length of time between saying each letter
    word_pause - length of time between saying each word.
    
    ctp - Fall 2016
    '''
    import os    # import os module, to use the 'say' command
    import time  # import the time module, to sleep (pause) the program
    import string # import string module for punctuation
    
    ICAO = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 
            'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 
            'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 
            'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 
            'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 
            'y':'yankee', 'z':'zulu'}     # create the dictionary for the ICAO alphabet
            
    fileReader = open(file)  # open and read the file
     
    exclude = set(string.punctuation)   # create a variable of punctuations
    wordList = []     # initialize word list
     
    for line in fileReader:     # loop through each line in the file
        wordList.append(line.split())       # create a list of lists, consisting of each word in the file
    
    fileReader.close() # close the file
    
    for lineList in wordList: #Loop through each list in the word list
        for word in lineList:             # loop through each word in the line
            word = ''.join(ch for ch in word if ch not in exclude)  # remove punctuation from the word             
            word = word.lower() # make the letters lower case
            time.sleep(word_pause) # pause  before beginning a new word
            for letter in word: # loop through each letter in the word
                translation = ICAO[letter] # translate the letter to the ICAO dictionary
                os.system('say'+translation) # speak the ICAO translation for that letter
                time.sleep(letter_pause) # pause after each letter
    
        
# 5.)
def hapax(file):
    '''
    This function reads in a file and searches for words that only occur
    once within the file, a hapax. It then returns all the hapaxs
    
    parameters:
    file - a file containing sentences.
    
    ctp - Fall 2016    
    '''
    import string            # used to check for punctuation
    
    
    fileReader = open(file)             # read the file
    
    lineList = []                       # initialize a list, consisting of the lines in file
    wordList = []                       # initialize a list, consisting of the letters in file
    
    for line in fileReader:             # loop over the lines in file
        lineList.append(line.strip())   # create a list consisting of each line in file
        
    fileReader.close()                  # close file
    
    for line in lineList:               # loop over the each string in lineList
        line = line.split()             # split the string into a list of words
        for word in line:               # loop through each word in the line
            exclude = set(string.punctuation)   # create a variable of punctuations
            word = ''.join(ch for ch in word if ch not in exclude)  # remove punctuation from the word             
            wordList.append(word.lower())    # append a lower case version of the word to a list of words
        
    
    wordDict = dict.fromkeys(wordList)  # create a dictionary consisting of each unique character in letterList
    
    for key in wordDict:                  # loop over each key value (character) in letterDict
        wordDict[key] = wordList.count(key) # Update the value in ltterDict to the count of each letter in letterList
        
    returnList = []         # initialize the returnList
    for key in wordDict:    # loop through the dictionary of words 
        if wordList.count(key) > 1: # for each word that occurs more than once
            continue                # continue through the loop
        returnList.append(key)      # if the word occurs once, append it to our returnList
        
    return returnList    # print the returnList


# 6.)
def numberedLines(file, newfilename):
    '''
    This function takes a text file, then creates a new text file
    Where the lines are numbered from 1 to n.
    
    Parameters:
    file - the text file that will be used to number and then create newfile
    newfilename  - the name of the new file to be created with numbered lines
    
    ctp - Fall 2016
    '''
    
    fileReader = open(file, 'r')    # read the text file  
    
    lineList = []       # initialize a list of lines
    returnList = []     # initialize a list of lines which will be numbered
    
    n = 1    # initialize our iterative variable n
    
    for line in fileReader:   # loop through each line in the file
        lineList.append(line) # append each line to the line list
    
    fileReader.close()    # close the original file
    
    for line in lineList:    # loop through each line in line list
        string = str(n) + ". " + line   # append the number n to the beggining of the line
        returnList.append(string)  # append this new numbered line to our numbered line list
        n += 1     # iterate to the next value of n    
    
    fileReader = open(newfilename, 'w')  # open the new file with write permissiong
    fileReader.writelines(returnList)    # write the numbered lines to the file
    
    fileReader.close()     # close the new file
    

# 7.)
def avgWordLen(file):
    '''
    This function calculates the average word length of a text
    stored in a file.  It calculates the number of words.
    Then calculates the total number of letters in all the words.
    Then takes the ratio of the total length over words to get the average.
    
    Parameters:
    file - a text file made up of words of varying length.
    
    ctp - Fall 2016
    '''
    import string           # import the string module for punctuation
    
    fileReader = open(file) # open the file
     
    wordList = []           # initialize the word list
    countList = []          # initialize a list consisting of the 'cleaned' word list, i.e. removed punctuation
        
    wordCount = 0           # intialize the count of words to 0
    
    for line in fileReader:  # loop through each line in the file
        for word in line.split():  # loop through each word in the line
            wordCount += 1         # count each word in the line
            wordList.append(word)  # append each word to our wordList
    
    fileReader.close() # close the file
    
    for word in wordList:        # loop through each word in the word list
            exclude = set(string.punctuation)  # create our exclusion variable, consisting of punctuation
            word = ''.join(ch for ch in word if ch not in exclude)   # Remove punctuation from our words          
            countList.append(word.lower())     # append our cleaned words to the count list.
    
    sumLen = 0   # initialize our total Length variable
    
    for word in countList:  # loop through each word in the cleaned list of words
        for letter in word: # loop through each letter int he cleaned word
            sumLen += 1     # count each letter
    
    return sumLen / wordCount # calculate the average length
    
# 8.)
def guess_number():
    '''
    This function, when run, starts a game called "Guess the Number".
    It randomly selects a number from 1 to 20.
    Then asks you to guess the number, and tells you if your guess is too high 
    or too low.  When you guess the number, it tells you how many guess it took.
    
    Parameters:
    None
    
    ctp - Fall 2016
    '''
    
    import random  # import the random package to generate a random number
    
    randNum = random.randrange(1,20) # generate a random number from 1 to 20.
    
    print('Hello!  What is your name?') # Ask the player his name
    
    name = input()  #Assign the player's answer to name
    
    print('Well, ' + name + ', I am thinking of a number between 1 and 20. Take a guess.') # Explain the game  

    
    for n in range(1,21):   # initialize a loop allowing the player twenty guesses.
        guess = int(input())   # read the player's guesses, and assign it to variable guess
        if guess > randNum:    # CHeck if the guess is greater than the answer
            print('Your guess is too high. Take a guess.') # if so, tell the player
        elif guess < randNum:  # check if guess is less then number
            print('Your guess is too low. Take a guess.') # if so tell the player
        else:     # if the guess is correct, exit the loop
            break
        
    print('Good job, ' + name + '! You guessed my number in ' + str(n) + ' guesses!') # tell the player the guess is correct, and how many guess it took



# 10.)
def Lingo():
    '''
    This function writes the logical game lingo. 
    There is a "Hidden" five character word, that the player
    must guess.  The player is given two types of hints after each guess.
    Either the word is wrapped in brackets or parenthesis.
    Brackets indicate the correct letter in the correct position.
    Parenthesis indicate the letter is in the word, but the wrong position.
    The game is over when the player guess the correct word.

    Parameters:
    None    
    
    ctp - Fall 2016

    '''
    import random    # import the random module, to randomize the choice of words
    words = ('table', 'flight', 'radar', 'would', 'woods', 'falls')  # create the word bank of hiddne words
    word = random.choice(words)  # randomly select opne of the hidden words
    
    for n in range(20):   # Allow twenty guesses
        
        guess = input()    # read in the player's guess
        
        guess = guess.lower()         # clean the guess to be lower case
        word  = word.lower()          # make sure the hidden word is lower case
        
        if len(guess) != 5:           # Check that the guess is 5 letters
            return "Please guess a five digit word"         # if it isn't ask for a 5 digit word
           
        returnVal = []      # initialize a list of return values
    
        for l in range(len(word)):  # create a loop, which loops through by the length of the hidden word
            if guess[l] == word[l]:  # check if the position is correct
                answer = "[" + guess[l] + "]"                # add the brackets
            elif guess[l] in word:     # if the position is not correct, check if the letter in the guess is in the hidden word
                answer = "(" + guess[l] + ")" # if so add the parenthesis
            else:                      # If the letter is not in the word
                answer = guess[l]      # the clue is to bracket or parenthsis
            
            returnVal.append(answer)   # Append this letter with clue to the return Value list
        
        returnVal = ''.join(returnVal)     # After loop through each letter in the hidden word, convert the return list to a string
        
        if guess == word:                 # If the guess is correct, print the bracketed word, and end game
            print("Clue: " + returnVal)
            break
        
        print("Clue: " + returnVal)    # if the guess is not correct, pring the clue, and continue with the next guess
        

# 11.)
def sentenceSplitter(file):
    '''
    This program splits a file into sentences.
    There are several hueristics this program follows to determine the end of a sentence.
    Once the end of the sentence is determined, the line ends and the rest of the text 
    begins on a new line.
    
    The hueristics are described in the code comments.
    
    Parameters:
    file - a file of text.
    
    ctp - Fall 2016
    '''
    
    import string    #import string module for punctuation.
    
    fileReader = open(file)   # open and read the file
    
    lineList = []    # initialize a list for each line in file.
    
    for line in fileReader:    # loop through each line
        line = line.replace('\n', ' ') # remove the line ends
        lineList.append(line)    # append each line to a list
    
    fileReader.close()   # close the file
    
    fileString = ''.join(lineList)    # convert the lis to a string, withough the '\n' line ends
    
    n = 0   # initialize an iterator
    old_n = 0 # intialize this variable used to select the starting position of each sentence.
    
    titleList = ['Mr','Mrs','Ms','Dr','Jr'] # create a title list 
    
    returnList = [] # intialize the final list to return
    
    for char in fileString:        # loop through each character in the string
        switch = 0     # this will indicate if it is the end of a sentence. 1 = end of sentence, 0 otherwise.
        
        if char in "." and not (n == 0 or n == len(fileString) - 1):  # Check if the character is a period, and not the first or second to last character in the string           
            switch = 1    # set the switch to 1, we will now go through the hueristics to check if it is not the end of a sentence.
            
            if fileString[n + 1] == " " and fileString[n + 2].islower():  # Hueristic 1: Periods followed by whitespace and then a lower case are not sentence boundaries                
                switch = 0  # if this is true, set swtich back to 0 and continue through the loop
                
            elif  fileString[n + 1].isnumeric():  # Hueristic 2: Periods foollowed by a digit with no intervening whitespace are not sentence boundaries                
                switch = 0  # if this is true, set switch back to 0, and continue through the loop
                
            elif fileString[n + 1] == " " and (fileString[n - 2].isupper() or fileString[n - 3].isupper()): # checks if the character 2 or 3 positions before the period are upper case
                if fileString[n-2:n] in titleList or fileString[n-3:n] in titleList:       # Hueristic 3: Checks for periods that come immediately after a person's title                
                    switch = 0 # if true set the switch back to 0 and continue through the loop
                    
            elif fileString[n-1] != " " and fileString[n+1] != " ": # Hueristic 4: check to see if the period is inside a sequence of letters with no adjacent whitepsace                
                switch = 0  # if true set switch back to 0 and continue through the loop.
        
            elif fileString[n+1] in string.punctuation: # Hueristic 5: check if other punctuation immediately follows the period.
                switch = 0 # If true set switch back to 0 and continue through loop.

        # After checking the 5 huersitics, need to check if the position is the end of the line.
        if switch == 1 or n == len(fileString)-1:  # It is the end of the line if switch = 1 (the position is a period that fails the 5 huersitic tests) or it is at the end of the string.
            returnList.append(fileString[old_n:n+1].strip()) # if this is true append the string segment from the period, back to the old_n position, to our output list
            old_n = n + 1  # reset the old_n variable to the new start of the sentence position
            
        n += 1 # iterate
    
    for line in returnList: # After going through the text file and separtating our sentence into elements in this list, 
        print(line)   # loop through the list and print each line.
