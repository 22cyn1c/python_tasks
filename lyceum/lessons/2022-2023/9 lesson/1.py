n = int(input())
t = set()
for i in range(n):
    a = input()
    t.add(a)
a = input()
if a not in t:
    print('OK')
else:
    print('TRY ANOTHER')