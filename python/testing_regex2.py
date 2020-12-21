import re

pattern = r"spam"
s = "eggspamsausagespam"

functs = [re.match, re.search]
def matchfunct(f, p, s):
    if f(p, s):
        print("match")
    else:
        print("no match")

map(matchfunct)
        
for f in functs:
    matchfunct(f, r"spam", "eggspamsausagespam")
