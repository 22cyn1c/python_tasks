a = int(input())
b = 0
c = 0
t = 0
for i in range(a + 1):
    if i == 0:
        continue
    if a % i == 0:
        for j in range(len(str(i))):
            b += int((str(i))[j])
            if b > c:
                c = b
                t = i
            elif b == c:
                if len(str(i)) < len(str(t)):
                    t = i
        b = 0
print(t)