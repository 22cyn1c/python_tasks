n, w, h = map(int, input().split())
if ((n * h * 2) + (w * h * 2)) % 16 == 0:
    print(((n * h * 2) + (w * h * 2)) // 16)
else:
    print(((n * h * 2) + (w * h * 2)) // 16 + 1)