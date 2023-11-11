a = int(input())
for i in range(a):
    b = input()
    if b[:3] == 'Не ' or b[:3] == 'не ':
        print(b[3:])
    else:
        print(b)