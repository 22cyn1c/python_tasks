k = int(input())
while k != 0:
    if k % 3 == 0 and k % 7 == 0:
        print('Караул!')
        break
    elif k % 3 == 0:
        print('несчастливое')
    elif k % 7 == 0:
        print('опасное')
    else:
        print(k)
    k = int(input())