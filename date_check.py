import re
#Function that checks the string for a date pattern
def check_date(a):
    n=''
    pattern1= '{}'.format(['-','/','.'])
    pattern= '\w+{}\w+{}\w+'.format(['-','/','.'],['-','/','.'] )
    if re.search(pattern1, a):
       se=re.search(pattern1, a)
       n= se.group()
    if re.search(pattern, a) or re.findall(r'\d+(?:-\d+)+',a):
       se = re.search(pattern, a)
       return 'd'
    else:
        return ''