n = int(input())
a = []
i = 1
while i < n:
    a.append(i)
    i = 10 * i + 1
print(', '.join([str(i ** 2) for i in a]))