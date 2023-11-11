n = int(input())
c = {}
for i in range(n):
    x, y = input().split()
    if (int(x) // 10, int(y) // 10) in c:
        c[(int(x) // 10, int(y) // 10)] += 1
    else:
        c[(int(x) // 10, int(y) // 10)] = 1
print(max(c.values()))