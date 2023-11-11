a = int(input())
n = 2
b = 1
t = 0
if a == 2:
    print(1)
elif a == 1:
    print(0)
else:
    while a > t:
        b += 1
        t = n**b
    if a == t:
        print(b)
    else:
        print("НЕТ")