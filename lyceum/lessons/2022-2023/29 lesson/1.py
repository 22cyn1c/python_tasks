import pymorphy2
import sys

access = 'йцукенгшщзхъфывапролджэячсмитьбюё '
access += access.upper()
c = 0
a = sys.stdin.read()
b = ''
for i in a:
    if i in access:
        b += i
    else:
        b += ' '
a = b.split()
morph = pymorphy2.MorphAnalyzer()
for i in a:
    s = morph.parse(i)[0].normal_form
    if s == 'видеть' or s == 'увидеть' or s == 'примечать' or s == 'узреть' \
            or s == 'глядеть':
        c += 1
print(c)
