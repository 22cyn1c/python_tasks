"""
https://acmp.ru/index.asp?main=task&id_task=970
"""
a, b, c = map(int, input().split())
if a + b == c or a + c == b or b + c == a:
    print('YES')
else:
    print('NO')