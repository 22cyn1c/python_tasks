t = 10 ** 9
while True:
    a = input()
    b = len(a)
    if 'добр' in a:
        if b < t:
            t = b
    if 'Бэггинс' in a:
        break
if t == 10 ** 9:
    print(0)
else:
    print(t)