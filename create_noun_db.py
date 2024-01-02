import sqlite3
from NaivePOS.MySQL import *
q= SQL("check_db.db")
q.execute("CREATE TABLE cities(city text, country text, state text)")
q.execute("CREATE TABLE names (name text, email text, phone text)")
q.execute("CREATE TABLE companies (name text, type text, category text)")
f= open("names.txt", "r")
for line in f:
    name = []
    line= line.split()
    for word in line:
            if word.isupper():
                name.append(word)
    name= ' '.join(name)
    for word in line:
            pattern= '@'
            if re.search(pattern, word) or word== '-':
                email= word
            pattern= '{}'.format([123456789])
            if re.search(pattern, word) or word== '-':
                number= word
    r= "INSERT INTO names VALUES ('{}', '{}', '{}')".format(name, email, number)
    q.execute(r)
g= open("us_companies.txt", "r")
for line in g:
    line= punc(line)
    name= []
    category= []
    line= line.split()
    type= ["Private", "Public", "Partnership"]
    for i in range(len(line)):
        if line[i] in type:
            ty= line[i]
            break
    for j in range(i):
        name.append(line[j])
    name= ' '.join(name)
    for k in range(i+1, len(line)):
        category.append(line[k])
    category= ' '.join(category)
    #print(name, ty, category)
    r = "INSERT INTO companies VALUES ('{}', '{}', '{}')".format(name, ty, category)
    q.execute(r)
qu= q.execute("SELECT * FROM companies")
print(qu)
h= open("world-cities.txt", "r")
for line in h:
    city= []
    country=[]
    state=[]
    start=0
    line=line.split()
    i=0
    flag=0
    for word in line:
        i+=1
        if word=='_':
            if flag==1:
                if word=='_':
                    for j in range(start, i-1):
                        country.append(line[j])
                        flag=2
                    start1= i
                    continue
            if flag==2:
                if word=='_':
                    for j in range(start1, i-1):
                        state.append(line[j])
                    continue
            for j in range(i-1):
                city.append(line[j])
                flag=1
                start=i
    city= ' '.join(city)
    country= ' '.join(country)
    state= ' '.join(state)
    for char in city:
        if char== '-':
            char= char.replace('-', ' ')
    for char in country:
        if char== '-':
            char= char.replace('-', ' ')
    for char in state:
        if char== '-':
            char= char.replace('-', ' ')
    city= punc(city)
    state= punc(state)
    country= punc(country)
    r = "INSERT INTO cities VALUES ('{}', '{}', '{}')".format(str(city), str(country), str(state))
    cursor.execute(r)
q.conn.commit()
p= "SELECT * FROM cities"
cursor.execute(p)
print(cursor.fetchall())