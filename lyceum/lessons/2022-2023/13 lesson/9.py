n = int(input())
s = []
for i in range(n):
    a = input()
    s.append(a)
n = int(input())
ss = []
for i in range(n):
    a = input()
    ss.append(a)
for el in ss:
    if el in s:
        print(el)