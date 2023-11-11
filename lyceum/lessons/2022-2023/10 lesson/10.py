a = input()
b = int(input())
if b > 0 and b <= len(a):
    print(a[b - 1])
else:
    print('ОШИБКА')