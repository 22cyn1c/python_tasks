a = input()
b = True
for i in a:
    if i == '0':
        print('NO')
        b = False
        break
if b:
    print('YES')