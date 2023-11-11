n = int(input())
for i in range(n):
    for u in range(n):
        print((i + 1) * (u + 1), end='\t')
    print()