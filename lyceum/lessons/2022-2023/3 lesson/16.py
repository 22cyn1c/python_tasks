a = int(input())
b = str(a // 100 + a // 10 % 10)
c = str(a // 10 % 10 + a % 10)
if int(b) > int(c):
    print(b + c)
else:
    print(c + b)