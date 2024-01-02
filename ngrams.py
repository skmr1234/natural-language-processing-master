#Function to make an input into ngrams
def make_ngram(text, num, rep):
        new_words= []
        new=[]
        text= text.lower().split()
        #Bigram
        if num == 2:
            for i in range(0, len(text)-1):
                new_words.append("{} {}".format(text[i], text[i+1]))
        #Trigram
        elif num == 3:
            for i in range(0, len(text)-2):
                new_words.append("{} {} {}".format(text[i], text[i+1], text[i+2]))
        #Separate the words with given special character
        for word in new_words:
            new_w=''.join(word)
            new_w= new_w.replace(' ', rep)
            new.append(new_w)
        return new