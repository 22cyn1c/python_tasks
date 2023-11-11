d = int(input())
m = int(input())
y = int(input())
if m == 1 or m == 2:
    m += 10
    y -= 1
else:
    m -= 2
c = y // 100
y %= 100
print((d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7)