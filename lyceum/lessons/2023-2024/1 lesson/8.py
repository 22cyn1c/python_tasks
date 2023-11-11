n = int(input())
a = []
b = []
le = 10 ** 9
r = 0 - 10 ** 9
t = 0 - 10 ** 9
bo = 10 ** 9
l1 = ''
r1 = ''
t1 = ''
bo1 = ''
for i in range(n):
    x, y = map(int, input().split())
    if y > 0:
        if abs(x) > y:
            print(f'({x}, {y})')
    else:
        if 0 - abs(x) < y:
            print(f'({x}, {y})')
    if x < le:
        l1 = 'left: (' + str(x) + ', ' + str(y) + ')'
        le = x
    if x > r:
        r1 = 'right: (' + str(x) + ', ' + str(y) + ')'
        r = x
    if y > t:
        t1 = 'top: (' + str(x) + ', ' + str(y) + ')'
        t = y
    if y < bo:
        bo1 = 'bottom: (' + str(x) + ', ' + str(y) + ')'
        bo = y
print(l1)
print(r1)
print(t1)
print(bo1)