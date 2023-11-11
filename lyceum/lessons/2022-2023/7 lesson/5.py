d = int(input())
c = 0
co = 0
while d != 0:
    co += 1
    c += d
    if c == 10:
        b = co
        print(b)
        break
    d = int(input())