a = input()
n = int(input())
t = 0
for i in range(n):
    b = input()
    if 'туннел' in b or a in b:
        t += 1
if t >= 3:
    print('МЫСЛЬ ЕСТЬ!')
else:
    print('ПОСИДИМ ЕЩЕ')
print((n - t) / n * 100)