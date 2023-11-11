n = int(input())
for i in range(n):
    c = [int(i) for i in input().split()]
    p = []
    while c:
        nc = max(c)
        if nc == c[0]:
            p.append(c.pop(0))
        elif nc == c[-1]:
            p.append(c.pop(-1))
        else:
            p = ['НЕТ']
            break
    print(*p)
