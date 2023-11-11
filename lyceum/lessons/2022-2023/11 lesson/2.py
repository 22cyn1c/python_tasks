a = input()
b = input()
n = int(input())
if len(a) > len(b):
    for i in range(len(b), len(a), n):
        print(i, end=' ')
elif len(b) > len(a):
    for i in range(len(a), len(b), n):
        print(i, end=' ')