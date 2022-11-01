a = int(input())
b = 0
for i in range(a):
    if a % (i + 1) == 0:
        b += i + 1
print(b)