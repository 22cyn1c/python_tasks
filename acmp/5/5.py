a = int(input())
b = list(map(int, input().split()))
set1 = list()
set2 = list()
c = 0
co = 0
for elem in b:
    if elem % 2 != 0:
        set1.append(elem)
        c += 1
    elif elem % 2 == 0:
        set2.append(elem)
        co += 1
for elem in set1:
    print(elem, end=' ')
print()
for elem in set2:
    print(elem, end=' ')
print()
if c <= co:
    print('YES')
else:
    print('NO')
'''
https://acmp.ru/index.asp?main=task&id_task=5
'''