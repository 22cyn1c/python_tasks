a = input().lower()
t = 0
for i in a:
    p = a.count(i)
    if p > t:
        t = p
print(t)