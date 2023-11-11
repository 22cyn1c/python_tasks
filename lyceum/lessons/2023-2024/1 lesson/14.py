import sys


co = 0
a = False
for i in sys.stdin:
    i = i.split()
    for j in i:
        j = j.lower()
        if 'далек' == j or 'далеки' == j or 'далека' == j or 'далеков' == j or 'далеку' == j or 'далекам' == j or\
                'далеком' == j or 'далеками' == j or 'далеке' == j or 'далеках' == j:
            co += 1
            break
print(co)