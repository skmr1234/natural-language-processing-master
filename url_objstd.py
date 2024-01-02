import time
from NaivePOS.defpunc import *
from NaivePOS.pat_search import *

#Open file with URLs
def remove_url(text):
    file1= open('url.txt').read().split("\n")
    #Get pattern and search
    for c in file1:
            pattern= '[\.]{}+?'.format(c)
            #print(pattern)
            text= pat_search(pattern, text)
    pattern= 'www|http'
    for i in range(0, len(pattern)):
            text= pat_search(pattern, text)
    text= punc(text)
    return text
#To remove punctuations
#a= punc(a).split()
def obj_std(text):
    text=text.split()
    #Dictionary with abbreviations:
    abb_dict= {'abt': 'about', 'abbr': 'abbreviation', 'acdnt': 'accident', '2': 'to', 'ack': 'acknowledgment', 'acpt': 'accept', 'addr': 'address', 'admin': 'administrator', 'adminr': 'administrator', 'aka': 'also known as', 'app': 'application', 'atm': 'at the moment', 'atb': 'all the best', 'awsm' : 'awesome', 'b4': 'before', 'bae': 'before anyone else', 'bb': 'baby', 'bby': 'baby', 'bbq': 'barbeque', 'bc': 'because', 'b/c': 'because', 'bday': 'birthday', 'b-day': 'birthday', 'bf': 'boyfriend', 'bff': 'best friend forever', 'bib': 'boss is back', 'bil': 'brother in law', 'bion': 'believe it or not', 'bol': 'best of luck','br': 'best regards', 'brb': 'be right back','bt': 'but',  'cb': 'coffee break', 'cmb': 'call me back', 'cu':'see you', 'dk': 'dont know', 'dm': 'direct message', 'em': 'email', 'ema': 'email adress', 'faq':'frequently asked questions', 'fb': 'facebook', 'fil': 'father in law', 'fyi' : 'for your information', 'gtg': 'got to go' , 'g2g': 'got to go', 'gb': 'goodbye', 'gn': 'goodnight', 'gm':'good morning', 'h-bday': 'happy birthday', 'idk': 'I dont know', 'idc': 'I dont care', 'ik': 'I know' , 'k': 'okay', 'kk': 'okay, okay', 'lol': 'laughing out loud', 'nthing': 'nothing', 'nvm':'never mind', 'ofc': 'of course', 'omg':'oh my God', 'os': 'operating system', 'pls' : 'please', 'plz': 'please', 'pic' : 'picture', 'r': 'are','rip': 'rest in peace', 'rofl': 'rolling on floor laughing' , 'rt': 'retweet', 'sup': 'whats up', 'srsly' : 'seriously' , 'sry': 'sorry' , 'ty' : 'thank you' , 'txt': 'text', 'thx': 'thanks', 'tyt': 'take your time', 'ttyl': 'talk to you later', 'u': 'you', 'y': 'why', 'wbu':'what about you', 'yr': 'your'}
    new_words= []
    #Retrieving the word from it's abbreviation:
    for word in text:
            if word in abb_dict:
                new_word= abb_dict[word]
                new_words.append(new_word)
            else:
                new_words.append(word)
    new_text= ' '.join(new_words)
    text=new_text
    #Remove special characters
    #pattern= '[@#$%^&*]'
    '''for i in range(0, len(pattern)):
        text= pat_search(pattern, text)'''
    return text

#Function to remove noise words
'''def remove_noise(filename, text):
    #Open file with noise words
    file1= open(filename).read().split('\n')
    for word in file1:
        for value in text:
                if str(value)== str(word):
                    a.remove(value)
    noise_free= ' '.join(a)
    return noise_free
a= remove_noise("noise.txt",a)
print(a)
print("date_check.py taken is: ", time.time()- start_time)'''
