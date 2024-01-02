from ngrams import *

from NaivePOS.MySQL import *

q= SQL("check_db.db")
def noun_check(nouns):
    id= {}
    #Make lists of names, companies and cities databases
    n= q.exec("SELECT NAME, EMAIL, PHONE FROM names")
    c= q.exec("SELECT NAME FROM COMPANIES")
    d= q.exec("SELECT CITY, COUNTRY, STATE FROM CITIES")
    nouns= ' '.join(nouns)
    #Make ngrams with nouns
    under= make_ngram(nouns, 2, '_')
    under3= make_ngram(nouns, 3, '_')
    for word in under3:
        under.append(word)
    nouns = nouns.split()
    #Append the words to input list
    for word in under:
        if word!='':
            word= ''.join(word)
            nouns.insert(0, word)
    for name in nouns:
        if len(name) == 1:
            continue
        flag = 0
        #To check if word is a name
        for word in n:
            word= ' '.join(word)
            #Make ngrams with the database names
            w= make_ngram(word, 2, '_')
            a= make_ngram(word, 3, '_')
            for wo in a:
                if wo!= '':
                    w.insert(0, wo)
            for i in range(len(w)):
                if name== w[i]:
                    id[name]= 'Name'
                    flag=1
                    break
            #Check individual names if entire name not found
            word= word.split()
            for i in range(len(word)):
                if name.upper()== word[i]:
                    id[name]= 'Name'
                    flag=1
                    break
        if flag==1:
            continue
        #To check if word is a city
        for word in d:
            word= ''.join(word[0])
            #Make ngrams with the database cities
            w= make_ngram(word, 2, '_')
            a= make_ngram(word, 3, '_')
            for wo in a:
                if wo!= '':
                    w.insert(0, wo)
            for i in range(len(w)):
                if name== w[i]:
                    id[name]= 'City'
                    flag=1
                    break
            if name.title()== word:
                    id[name] = 'City'
                    break
        if flag==1:
            continue
        #To check if word is a country or State
        for word in d:
            w_country = ''.join(word[1])
            #Make ngrams from countries and states database
            w_c = make_ngram(w_country, 2, '_')
            a1= make_ngram(w_country, 3, '_')
            for wo in a1:
                if wo!='':
                    w_c.insert(0, wo)
            w_state= ''.join(word[2])
            w_s= make_ngram(w_state, 2, '_')
            a2= make_ngram(w_state, 3, '_')
            for wo in a2:
                if wo!='':
                    w_s.insert(0, wo)
            for i in range(len(w_c)):
                if name == w_c[i]:
                    id[name.title()]= "Country"
                    flag=1
                break
            for i in range(len(w_s)):
                if name== w_s[i]:
                    id[name.title()]= "State"
                    flag=1
                    break
            if name.title()== word[1]:
                    id[name]= 'Country'
            elif name.title()== word[2]:
                    id[name]= 'State'
                    break
        if flag==1:
            continue
        #To check if word is a company
        for word in c:
            word= ' '.join(word)
            w = make_ngram(word, 2, '_')
            for i in range(len(w)):
                if name == w[i]:
                    id[name] = 'Company'
                    flag = 1
                    break
            #print(word)
            if name==word:
                    id[name]= 'Company'
                    break
    if len(id)!=0:
        print(id)