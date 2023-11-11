n = int(input())
d = 0
for i in range(n - 1):
    if n % (i + 1) == 0:
        d += 1
        print(i + 1, end=' ')
print(n)
if d == 1:
    print('ПРОСТОЕ')
else:
    print("НЕТ")