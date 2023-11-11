n = int(input())
a = int(input())
b = int(input())
for i in range(n, a + 1, b):
    for j in range(n, a + 1, b):
        print(i, '+', j, '=', i + j, end='\t')
    print()