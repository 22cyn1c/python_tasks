t = [0] * 30000
s = input()
j = 0
for i in s:
    if i == '>':
        j = (j + 1) % 30000
    elif i == '<':
        j = (j + 29999) % 30000
    elif i == '+':
        t[j] = (t[j] + 1) % 256
    elif i == '-':
        t[j] = (t[j] + 255) % 256
    elif i == '.':
        print(t[j])