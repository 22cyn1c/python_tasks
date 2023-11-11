a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
for i in a:
    i = str(i)
    for f in b:
        f = str(f)
        if len(i) == 1:
            if len(f) == 1:
                if int(i) != int(f):
                    print(f'0{i}:0{f}')
            else:
                if int(i) != int(f[0]) + int(f[1]):
                    print(f'0{i}:{f}')
        elif len(f) == 1:
            if int(i[0]) + int(i[1]) != int(f):
                print(f'{i}:0{f}')
        else:
            if int(i[0]) + int(i[1]) != int(f[0]) + int(f[1]):
                print(f'{i}:{f}')