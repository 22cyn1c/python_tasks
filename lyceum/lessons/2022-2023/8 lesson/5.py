n = int(input())
maximin = 0
k = 0
for i in range(n):
    a = int(input())
    mb = 10**9
    for j in range(a):
        b = int(input())
        if mb > b:
            mb = b
    if maximin < mb:
        maximin = mb
        k = i + 1
print(k, maximin)