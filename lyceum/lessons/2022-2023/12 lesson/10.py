a = int(input())
for i in range(a):
    b = input()
    if b[:2] == '%%':
        print(b[2:])
    elif b[:4] == '####':
        continue
    else:
        print(b)