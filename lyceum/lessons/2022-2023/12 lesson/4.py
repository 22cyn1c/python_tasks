a = input()
b = 0
t = 10000000
str_max = set()
str_min = set()
while a != 'стоп':
    if len(a) > b:
        b = len(a)
        str_max = a
    if len(a) < t:
        t = len(a)
        str_min = a
    a = input()
is_find = True
for i in str_min:
    if i not in str_max:
        is_find = False
        break
if is_find:
    print('ДА')
else:
    print('НЕТ')