import re
patt = r"(spam)*egg"
b = re.search(patt, "eggspambaconegg")
if b:
    print(b.group())
