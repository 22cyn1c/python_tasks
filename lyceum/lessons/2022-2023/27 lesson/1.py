a = input().split()
b = []
for i in a:
    b.append(255 - int(i))
print(*b)