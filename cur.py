import re
def currency(a):
   a= a.split()
   i=0
   wo=''
   for word in a:
      curr= ['$', '€', '£', 'ლ', '₹', '৳', '¥']
      cur= {'$': ' Dollars', '€': ' Euros', '£':' British Pounds', 'ლ':' Georgian Lari', '₹': ' Indian Rupees', '৳': ' Bangladeshi taka', '¥': ' Chinese yuan'}
      pattern= '{}'.format(curr)
      if re.search(pattern, word):
        se= re.search(pattern, word)
        print(se.group())
        if se:
          wo=word.replace(se.group(), cur.get(se.group()))
          a.remove(word)
          a.insert(i, wo)
      i+=1
   a=' '.join(a)
   return a