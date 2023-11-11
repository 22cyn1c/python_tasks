a = input()
b = 0
for i in range(len(a)):
    if ord(a[i]) != 95 and not 96 < ord(a[i]) < 123 and not 47 < ord(a[i]) < 58:
        print('Неверный символ:', a[i])
        b = 1
        break
if b == 0:
    print('OK')