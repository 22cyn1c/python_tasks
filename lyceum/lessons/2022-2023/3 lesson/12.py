a = float(input())
b = float(input())
c = input()
if c == '-':
    print(a - b)
elif c == '+':
    print(a + b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b != 0:
        print(a / b)
    else:
        print('888888')
else:
    print('888888')