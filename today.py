import datetime
from ngrams import *
now= datetime.datetime.now()
#days= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
#month= ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
words= {'next': '+', 'following': '+', 'coming': '+', 'previous': '-', 'last': '-'}
dwmy= {'day': 'd', 'week': 'w', 'month': 'm', 'year': 'y'}
a= input("Enter a string: ").lower().split()
for word in a:
    if word == "today":
        print(now.strftime("%d-%m-%Y %H:%M"))
    elif word == "tomorrow":
        b = now.day + 1
        print("{}-{}-{}".format(b, now.month, now.year))
a= ' '.join(a)
a= make_ngram(a, 2, '_')
for w in a:
    w= w.split('_')
    s=''
    n=''
    if w[0] in words:
        n= words.get(w[0])
    if w[1] in dwmy:
        s= dwmy.get(w[1])
    pattern= '{}{}'.format(n, s)
    if n and s:
        print(pattern)
