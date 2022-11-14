a = int(input())
b = list(map(int, input().split()))
for i in range(a):
    print(b[-(i + 1)], end=' ')