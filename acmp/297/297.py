n = input()
var = [i for i in n]
b = 0
for i in range(len(var)):
    if var[i] == '6' or var[i] == '0' or var[i] == '9':
        b = b + 1
    elif var[i] == '8':
        b = b + 2
print(b)
"""
https://acmp.ru/index.asp?main=task&id_task=297
"""