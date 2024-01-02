#POS Tags
c= ['n', 'v', 'a', 's', 'r']
nc=[]
#Initialize the counts to zeroes
for i in range(len(c)):
    nc.append(0)
#Open WordNet Database
with open('WordNetData.txt', 'r') as f:
    for word in f:
            count=0
            word= word.split()
            #value= "{} 0\n".format(word[0])
            #Get the total count of each class
            for i in range(len(c)):
                if word[1]==c[i]:
                            count+=1
                            nc[i]+=count
res=0
p=[]
#To find total number of words in the database
for i in range(len(c)):
    res+=nc[i]
#To calculate probability
for i in range(len(c)):
    p.append(nc[i]/res)