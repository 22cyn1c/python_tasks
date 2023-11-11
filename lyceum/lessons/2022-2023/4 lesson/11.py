pas = input()
pas1 = input()
if len(pas) < 8:
    print("Короткий!")
elif '123' in pas:
    print("Простой!")
elif pas != pas1:
    print("Различаются.")
else:
    print("OK")