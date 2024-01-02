import re
#Function to search for a pattern and remove it
def pat_search(pattern, text):
    se = re.search(pattern, text)
    if se:
        text = text.replace(se.group(), '')
    return text