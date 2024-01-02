import re
import datetime
now= datetime.datetime.now()
days= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
month= {'1':'31', '2':'28', '3':'31', '4':'30', '5':'31', '6':'30', '7':'31', '8':'31', '9':'30', '10':'31', '11':'30', '12':'31'}
cur_day= now.day
cur_month= now.month
cur_year= now.year
for i in range(6):
    b= input("Enter value: ")
    a = ['0', '9', '*', '*', '?', '*']
    if b.lower()== 'daily':
        a[4]= '*'
        print(a)
    elif b.lower()== 'tomorrow':
            d= month.get(str(cur_month))
            if cur_day<int(d):
                mon= cur_month
                day= now.day +1
            else:
                mon= (cur_month +1)%12
                day=1
            if cur_month== 12 and int(d)==cur_day:
                cur_year= cur_year+1
            a[2]= day
            a[3]= mon
            a[5]= cur_year
            print(a)
    elif b.lower()== 'weekly':
            a[2]= '*/7'
            print(a)
    elif b.lower()== 'hourly':
            a[1]= '*'
            print(a)
    elif b.lower()== 'monthly':
            a[2]= cur_day
            print(a)
    elif b.lower()== 'yearly':
            a[2]= cur_day
            a[3]= cur_month
            print(a)
print(a)




