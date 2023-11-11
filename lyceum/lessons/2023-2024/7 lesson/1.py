from random import choice

f = open('lines.txt')
s = f.readlines()
if s:
    print(choice(s))
f.close()