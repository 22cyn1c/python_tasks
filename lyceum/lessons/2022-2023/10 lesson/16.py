a = input()
b = 0
t = 0
for i in range(len(a)):
    if a[i] == 'о':
        b += 1
        if b > t:
            t = b
    else:
        b = 0
print(t)