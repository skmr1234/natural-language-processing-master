import re

def mod_stem(text):
    a = text.lower()
    consonants = []
    #Obtaining all consonants from input text
    for char in a:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            continue
        else:
            consonants.append(char)
    #Patterns to find measure of the word
    pattern0 = '^{}*?[aeiou]*?$'.format(consonants)
    pattern1 = '^{}*?[aeiou]+?{}+?[aeiou]*?$'.format(consonants, consonants)
    pattern2 = '^{}*?[aeiou]+?{}+?[aeiou]+?{}+?[aeiou]*?$'.format(consonants, consonants, consonants)

    #Function to get the measure of the word or word part
    def getm(a):
        #Function to search text with the patterns
        def get_m(pattern, a):
            if re.search(pattern, a):
                se = re.search(pattern, a)
                return 1
        if (get_m(pattern0, a)):
            m = 0
        elif (get_m(pattern1, a)):
            m = 1
        elif (get_m(pattern2, a)):
            m = 2
        else:
            m = 3;
        return m


    m = getm(a)
    a = a.split()

    new_words = []

    #Step 1a
    def step1a(a):
        firsta_dict = {'sses': 'ss', 'ies': 'i', 'ss': 'ss', 's': ''}
        for key in firsta_dict:
            pattern = '{}$'.format(key)
            d = a
            pattern1 = 'ies$'
            if re.search(pattern1, d):
                d = re.sub(pattern1, '', d)
                m1 = getm(d)
                if m1==0:
                    patter= 's$'
                    a= re.sub(patter, '', a)
                    continue
                if m1>0:
                    a= re.sub(pattern1, 'y', a)
                    continue
            d = re.sub(pattern, '', d)
            m1= getm(d)
            if m1 > 0:
                if re.search(pattern, a):
                    se = re.search(pattern, a)
                    string = firsta_dict.get(key)
                    a = re.sub(pattern, string, a)
                    break
        return a
        # print(a)

    #Step 1b
    def step1b(a):
        firstb_dict = {'at': 'ate', 'bl': 'ble', 'iz': 'ize'}
        firstb1_dict = {'eed': 'ee', 'ed': ''}
        flag = 0
        d = a
        for key in firstb1_dict:
            pattern = '{}$'.format(key)
            d = re.sub(pattern, '', d)
            m1 = getm(d)
        if (m1 > 0):
            pattern = 'eed$'
            if re.search(pattern, a):
                se = re.search(pattern, a)
                a = re.sub(se.group(), 'ee', a)
                # new_words.append(a)
                # print(a)
            pattern1 = '[aeiou]+?{}*?ed$'.format(consonants)
            pattern2 = '[aeiou]+?{}*?ing$'.format(consonants)
            if re.search(pattern1, a):
                se = re.search(pattern1, a)
                a = re.sub('ed$', '', a)
                # new_words.append(a)
                # print(a)
                flag = 1
            elif re.search(pattern2, a):
                se = re.search(pattern2, a)
                a = re.sub('ing$', '', a)
                # new_words.append(a)
                # print(a)
                flag = 1
            # print(flag)
            if flag == 1:
                for key in firstb_dict:
                    pattern = '{}$'.format(key)
                    # print(pattern)
                    if re.search(pattern, a):
                        se = re.search(pattern, a)
                        string = firstb_dict.get(key)
                        a = re.sub(se.group(), string, a)
                        # new_words.append(a)
                        # print(a)
                        # break
                for key in consonants:
                    if key not in ['l', 's', 'z']:
                        pattern = '{}{}$'.format(key, key)
                        if re.search(pattern, a):
                            se = re.search(pattern, a)
                            a = re.sub(se.group(), key, a)
                            # new_words.append(a)
                            # print(a)
                            # break
                m1= getm(a)
                if (m1 == 1):
                    for key in consonants:
                        f = []
                        if key not in ['w', 'x', 'y']:
                            f = key
                            pattern = '{}[aeiou]{}$'.format(consonants, f)
                            #print(pattern)
                            if re.search(pattern, a):
                                se = re.search(pattern, a)
                                a = list(a)
                                a.append('e')
                                a = ''.join(a)
                                # new_words.append(a)
                                # print(a)
                                # break
        return a

    #Step 2
    def step2(a):
        #global new_words
        second_dict = {'ational': 'ate', 'tional': 'tion', 'enci': 'ence', 'anci': 'ance', 'izer': 'ize', 'abli': 'able',
                       'alli': 'al', 'entli': 'ent', 'eli': 'e', 'ousli': 'ous', 'ization': 'ize', 'ation': 'ate',
                       'ator': 'ate', 'alism': 'al', 'iveness': 'ive', 'fulness': 'ful', 'ousness': 'ous', 'aliti': 'al',
                       'iviti': 'ive', 'biliti': 'ble'}
        for key in second_dict:
            pattern = '{}$'.format(key)
            # print(pattern)
            if re.search(pattern, a):
                d = a
                d = re.sub(pattern, '', d)
                m1 = getm(d)
                se = re.search(pattern, a)
                # print(se.group())
                if m1 > 0:
                    a = re.sub(se.group(), second_dict.get(key), a)
                    # new_words.append(a)
                    # print(a)
                break
        return a

    #Step 3
    def step3(a):
       #global new_words
        third_dict = {'icate': 'icate', 'ative': '', 'alize': 'al', 'iciti': 'ic', 'ical': 'ic', 'ful': '', 'nes': ''}
        for key in third_dict:
            pattern = '{}$'.format(key)
            # print(pattern)
            if re.search(pattern, a):
                d = a
                d = re.sub(pattern, '', d)
                m1 = getm(d)
                se = re.search(pattern, a)
                # print(se.group())
                if m1 > 0:
                    a = re.sub(se.group(), third_dict.get(key), a)
                    # new_words.append(a)
                    # print(a)
                break
        return a

    #Step 4
    def step4(a):
        #global new_words
        fourth_dict = {'al': '', 'ence': '', 'er': '', 'ic': '', 'able': '', 'ible': '', 'ant': '', 'ement': '',
                       'ment': '', 'ent': '', 'sion': '', 'tion': '', 'ou': '', 'ism': '', 'iti': '', 'ous': '',
                       'ive': '', 'ize': ''}
        for key in fourth_dict:
            pattern = '{}$'.format(key)
            # print(pattern)
            if re.search(pattern, a):
                d = a
                d = re.sub(pattern, '', d)
                m1 = getm(d)
                se = re.search(pattern, a)
                # print(se.group())
                if m1 > 1 and se.group() == 'tion' or se.group() == 'sion':
                    a = re.sub('ion', fourth_dict.get(key), a)

                elif m1 > 1:
                    # print(se.group())
                    a = re.sub(se.group(), fourth_dict.get(key), a)
                # new_words.append(a)
                # print(a)
                break
        return a

    '''def step5a(a):
        global new_words
        pat = 'e$'
        d = a
        d = re.sub(pat, '', d)
        m1 = getm(d)
        print(m1)
        if m1 >=2:
            if re.search(pat, a):
                a = re.sub(pat, '', a)
        if m1 == 1:
            for key in consonants:
                f = []
                if key not in ['w', 'x', 'y']:
                    f = key
                    pattern = '{}[aeiou]{}$'.format(consonants, f)
                    if re.search(pattern, d):
                        break
                    else:
                        a = re.sub(pat, '', a)
        return a'''

    #Step 5b
    def step5b(a):
        #global new_words
        pat = 'll$'
        d = a
        d = re.sub(pat, '', d)
        m1 = getm(d)
        if m1 >= 1:
            if (re.search(pat, a)):
                a = re.sub(pat, 'l', a)
        new_words.append(a)


    # pattern3= '^{}*?[aeiou]+?{}+?[aeiou]+?{}+?[aeiou]+?{}+?[aeiou]*?$'.format(consonants, consonants, consonants, consonants)
    #Calling the function for each word of the text
    for word in a:
        b = step1a(word)
        c = step1b(str(b))
        #d=step1c(str(c))
        e = step2(str(c))
        f = step3(str(e))
        g = step4(str(f))
        #h=step5a(str(g))
        step5b(str(g))
    new_text = ' '.join(new_words)
    return new_text