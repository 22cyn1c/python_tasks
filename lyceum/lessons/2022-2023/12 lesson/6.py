a = int(input())
b = int(input())
for i in range(b):
    c = input()
    if len(c) > a:
        print(c[:a - 3] + '...')
    else:
        print(c)