a = input()
a = a.upper()
s = []
for el in a:
    s.append(el)
print('-'.join(s).replace('- -', ' '))