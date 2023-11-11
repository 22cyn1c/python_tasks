a = int(input())
b = 0
for i in range(a):
    d = input()
    if 'кот' in d or 'Кот' in d:
        b = 1
        print('МЯУ')
        break
if b == 0:
    print('НЕТ')