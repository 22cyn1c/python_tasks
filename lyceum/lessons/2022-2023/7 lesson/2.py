d = input()
c = 1
b = -1
while d != 'СТОП':
    if 'Кот' in d or 'кот' in d:
        if b == -1:
            b = c
    c += 1
    d = input()
print(b)