pas = input()
pas1 = input()
if len(pas) < 8:
    print("Короткий!")
elif pas != pas1:
    print("Различаются.")
else:
    print("OK")