"""
https://acmp.ru/index.asp?main=task&id_task=755
"""
s = list(map(int, input().split()))
if s[0] + s[1] < s[2]:
    print('Impossible')
else:
    print(-(s[2] - (s[1] + s[0])))