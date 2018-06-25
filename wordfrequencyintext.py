""" This is a data mining program--Our objective is to find out the frequency with which certain words appear in a text"""
"""Uses the traditional approach in which frequency of a single word is found and no dictionary is used"""

file = open('mydoc.txt','r')    # needless to say, if your document is stored in a different location from your Python installation, the path will have to be provided
book = file.read()

# After reading the document , one needs to convert everything to lower case by tokenising it

def tokenize():
    if book is not None:
        words = book.lower().split()
        return words
    else:
        return None

def count_word(tokens,token):
    count = 0
    for element in tokens:
        word = element.replace(","," ") # Remove punctuation
        word = word.replace(".","")
        word = word.replace("!","")
        word = word.replace("?","")
        if word == token:
            count += 1
    return count

# Tokenise the book

words = tokenize()

# Get the word count

word = 'creature'
frequency = count_word(words,word)
print('word: ['+ word + '] Frequency: ' + str(frequency))

