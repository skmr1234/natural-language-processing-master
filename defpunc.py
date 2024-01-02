import string
#Function that finds punctuations and removes it
def punc(a):
    for char in string.punctuation:
        a=str(a)
        a=a.replace(char, '')
    return a
