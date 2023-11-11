a = int(input())
c = 1
for i in range(a):
    b = input()
    if 'кот' in b:
        print(c, end=' ')
        for j in range(len(b)):
            if b[j:j + 3] == 'кот':
                print(j + 1)
                break
    c += 1