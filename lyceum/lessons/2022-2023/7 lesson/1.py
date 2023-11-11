a = int(input())
c = 1
b = 0
while c <= a:
    d = input()
    if 'Кот' in d or 'кот' in d:
        b += 1
    c += 1
if b > 0:
    print('МЯУ')
else:
    print('НЕТ')