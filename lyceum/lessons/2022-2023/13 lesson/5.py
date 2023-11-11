n = int(input())
s = ['щи', 'борщ', 'щавелевый суп', 'овсяный суп', 'суп по-чабански']
if n % 5 == 0:
    for i in range(n // 5):
        for el in s:
            print(el)
else:
    for i in range(n // 5):
        for el in s:
            print(el)
    b = n % 5
    s = s[:b]
    for el in s:
        print(el)