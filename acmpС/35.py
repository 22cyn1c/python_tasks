k = int(input())
for i in range(k):
    n, m = input().split()
    n = int(n)
    m = int(m)
    print(int(19 * m + (n + 239) * (n + 366) / 2))