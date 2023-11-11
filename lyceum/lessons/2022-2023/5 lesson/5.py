n = int(input())
while True:
    if n % 4 == 0:
        n -= 1
        print(1, n)
    else:
        print(n % 4, n - n % 4)
        n -= n % 4
    if n == 0:
        print('ИИ выиграл!')
        break
    k = int(input())
    while k > 3 or k < 1 or k > n:
        print('Некорректный ход:', k)
        k = int(input())
    n -= k
    print(n, k)
    if n == 0:
        print('Вы выиграли!')
        break
