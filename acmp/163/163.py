a = input()
if a[1] == '-':
    if a[0] == 'x':
        print(int(a[2]) + int(a[4]))
    elif a[2] == 'x':
        print(int(a[0]) - int(a[4]))
    else:
        print(int(a[0]) - int(a[2]))
else:
    if a[0] == 'x':
        print(int(a[4]) - int(a[2]))
    elif a[2] == 'x':
        print(int(a[4]) - int(a[0]))
    else:
        print(int(a[0]) + int(a[2]))