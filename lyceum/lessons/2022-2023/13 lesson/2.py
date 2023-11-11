n = int(input())
s = []
for i in range(n):
    a = input()
    s.append(a)
a = input()
for el in s:
    if a in el:
        print(el)