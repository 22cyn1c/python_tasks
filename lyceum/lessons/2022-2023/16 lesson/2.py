n = input().split()
m, k = input().split()
m = int(m)
k = int(k)
n = n[m:k + 1]
s = 0
for elem in n:
    s += int(elem) ** 2
print(s)
