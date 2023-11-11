d = input()
b = -1
c = 0
while d != 'СТОП':
    c += 1
    if 'кот' in d or 'Кот' in d:
        if b == -1:
            b = c
        print(b)
        break
    d = input()
if b == -1:
    print(b)