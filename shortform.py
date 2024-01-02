from pat_search import *
#Function to expand the contractions
def short_form(text):
    patterns= ["n\'t$", "\'ll$","\'m$", "\'re$", "\'s$", "\'ve$", "\'d"]
    text = text.split()
    a = []
    new = []
    for word in text:
        for i in range(len(patterns)):
            var= pat_search(patterns[i], word)
            if var!=word:
                break
        rep= {"n\'t$": "not", "\'ll$": "will", "\'m$": "am", "\'re$": "are", "\'s$": "is", "\'ve$": "have", "\'d": "had"}
        if var== 'ca':
            var=var.split()
            var.append('n')
        elif var== 'wo':
            var=var.split()
            var.append('will')
            var.pop(0)
        elif var== 'sha':
            var=var.split()
            var.append('shall')
            var.pop(0)
        if var!=word:
            var=''.join(var)
            var=var.split()
            var.append(rep.get(patterns[i]))
        a.append(var)
    for word in a:
        if list(word) == word:
            word = ' '.join(word)
        new.append(word)
    new = ' '.join(new)
    return new