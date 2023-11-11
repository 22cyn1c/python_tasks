a = input()
t = 0
r = 'я'
a = a.lower()
for i in a:
    p = a.count(i)
    if p >= t and i != ' ':
        if p == t:
            if ord(i) < ord(r):
                r = i
        else:
            t = p
            r = i
print(r)