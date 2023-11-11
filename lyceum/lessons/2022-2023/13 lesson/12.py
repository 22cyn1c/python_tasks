n = int(input())
p_l = []
n_l = []
for i in range(n):
    a = input()
    p_l.append(a)
    b = int(input())
    n_l.append(b)
n_l = n_l[::-1]
p_l = p_l[::-1]
for i in range(n):
    print(p_l[i], n_l[i])
