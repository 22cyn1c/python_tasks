n = int(input())
b = 0
p = 3.141592653589793
for i in range(n):
    b += 1 / (i + 1) ** 2
print(p ** 2 / b)
