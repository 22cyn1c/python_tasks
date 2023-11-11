n = int(input())
n1 = int(input())
a = input()
for g in range(n1):
    print(a, end='')
print()
for i in range(2, n):
    print(a, end='')
    for j in range(n1 - 2):
        print(' ', end='')
    print(a)
for s in range(n1):
    print(a, end='')