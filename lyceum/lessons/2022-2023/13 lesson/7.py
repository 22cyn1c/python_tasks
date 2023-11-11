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
b = 0
for el in s:
    for ele in ss:
        if ele in el:
            b += 1
    if b == len(ss):
        print(el)
    b = 0