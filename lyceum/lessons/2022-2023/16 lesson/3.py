n = int(input())
for i in range(n):
    a = input()
    p = a.find('кот')
    if p != -1:
        print(i + 1, p + 1)