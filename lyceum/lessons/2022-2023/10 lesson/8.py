a = int(input())
b = 0
while a <= 1000000000 and b != 1:
    b = int(str(a)[0])
    a *= b
print(a)
