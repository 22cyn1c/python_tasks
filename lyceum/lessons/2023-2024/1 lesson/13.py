import sys


co = 0
a = False
for i in sys.stdin:
    i = i.split()
    for j in i:
        j = j.lower()
        if j[:5] == 'далек':
            co += 1
            break
print(co)