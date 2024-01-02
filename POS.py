import operator
from check_nouns import *
from cur import *
from date_check import *
from defpunc import *
from mod_stem import *
from ngrams import *
from pc import *
from shortform import *
from NaivePOS.MySQL import *
from NaivePOS.url_objstd import *

x= input("Enter a string: ")
start_time= time.time()
#Expand contractions from text
x= short_form(x)
#Check the string for any currency terms and expand
x= currency(x)
#Object Standardization and URL Removal
x= obj_std(x)
x= remove_url(x)
#Make the text into ngrams
under= make_ngram(x, 2, '_')
x= x.split()
first= x[0]
new_dict = []
#Check the words in the sentence for a date pattern
for l in x:
    dat = check_date(l)
    if dat == 'd':
        new_dict.append((l, 'd'))
        x.remove(l)
x=' '.join(x)
#Remove punctuations
x= punc(x).split()
#Join the ngrams as part of input text in the first position so they are checked first
for word in under:
    if word!='':
        word= ''.join(word)
        x.insert(0, word)
#Open WordNet database
q= SQL("mydatabase.db")
#Get the class and it's corresponding count from database
ccount= q.exec('SELECT CLASS, SUM(COUNT) FROM word_count3 GROUP BY CLASS')
i=1

#Loop to find POS tag by Naive Bayes for each word in input text
for lin in x:
    l= str(lin)
    wcount= q.exec("SELECT WORD, SUM(COUNT), CLASS FROM word_count3 WHERE word= '%s'  GROUP BY CLASS"%(l))
    #print(wcount)
    #If word is not present in the database
    if len(wcount)==0:
        #Check if word is first word and is capitalized
        if lin==first and l.title()==l:
            l=l.lower()
            #Change the word to lower case and check database again
            wcount = q.exec("SELECT WORD, SUM(COUNT), CLASS FROM word_count3 WHERE word= '%s'  GROUP BY CLASS" % (l))
            #If word is still not found, assign it as noun
            if (len(wcount)==0):
                new_dict.append((l.title(), 'n'))
                continue
        #If word is capitalized, assign it as noun
        elif l.title()==l or l.upper()==l:
            new_dict.append((l, 'n'))
            continue
        #If word not present, stem the word with Porter Stemmer algorithm and check database again
        else:
            l= mod_stem(l)
            wcount = q.exec("SELECT WORD, SUM(COUNT), CLASS FROM word_count3 WHERE word= '%s'  GROUP BY CLASS" % (l))
            #If word is still not found, then assign it as unknown
            if (len(wcount)==0):
                new_dict.append((l, ''))
                continue
    #print("Wcount word is : ", wcount[0])
    tpf= {}

    for line in wcount:
        #Word
        wo= line[0]
        #Number of occurences
        count= line[1]
        #Class of the word
        cl= line[2]
        #print("Cl is: ", cl)
        pf=0
        for w in ccount:
            if cl==w[0]:
                #Naive Bayes formula to find probability of the class for the given word
                #The variable 'res' has the count of all the words in the database
                pf = (count + 1) / (w[1] + res)
                #print("Pf is : ", pf)
            #Assign the probability to it's class in the dictionary tpf
            for i in range(len(c)):
                if cl == c[i]:
                    #print("P[i] and class is: ", p[i], cl)
                    tpf[cl]= pf
                    break
    #print("TPF is : ", tpf)
    #If the word has no class it belongs to, then append as unknown
    if(len(tpf)==0):
        new_dict.append((wo, ''))
        continue
    #Find maximum value from dictionary
    great= max(tpf.items(), key= operator.itemgetter(1))[0]
    #print("Great value is: ", great)
    #Assign the class that has maximum probability
    new_dict.append((wo, great))
    i+=1
new_list=[]
for word in new_dict:
    new_list.append(word)
#Remove extra unidentified ngrams
for word in new_list:
    if '_' in word[0] and word[1]=='':
            new_dict.remove(word)
print(new_dict)
nouns= []
#Check if the nouns are names, cities or companies
for word in new_dict:
    if word[1]=='n':
        nouns.append(word[0].title())
noun_check(nouns)
print(time.time()- start_time)