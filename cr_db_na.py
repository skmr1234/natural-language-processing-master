from NaivePOS.MySQL import *
import string
q= SQL("database.db")
q.execute('''CREATE TABLE word_count3 (word text,count integer, class text, word_id integer, pos_id integer)''')
f= open("WordNetData.txt", "r")
for line in f:
        for char in string.punctuation:
            line= line.replace(char, '_')
        line= line.split()
        print(line)
        print(line[1])
        print(line[2])
        print(line[3])
        s= str(line[0])
        count= 1
        '''if len(line)==1:
            continue'''
        r= "INSERT INTO word_count3 VALUES ('{}', '{}', '{}', '{}', '{}')".format(s, count, str(line[1]), line[2], line[3])
        q.execute(r)
