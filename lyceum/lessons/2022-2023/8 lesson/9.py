n = int(input())
for i in range(n):
    for j in range(i + 1):
        print('Осталось секунд:', i - j)
    print('Пуск', i + 1)