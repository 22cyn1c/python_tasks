f = open("foreigner.txt", 'r')
fr = f.read()
s = open("signs.txt", 'w')
mn = set()
for i in fr.split('; '):
    a = i.split()[:2]
    a = ' '.join(a).lower()
    mn.add(a)
for i in mn:
    s.write(i + '\n')
f.close()
s.close()