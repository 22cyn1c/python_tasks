a = input()
b = int(input())
c = input()
if len(a) >= b and len(c) == 1 and 1071 < ord(c) < 1104 and b > 0:
    if a[b - 1] == c:
        print('ДА')
    else:
        print('НЕТ')
else:
    print('ОШИБКА')