a = ''
while a != "OK":
    pas = input()
    pas1 = input()
    if len(pas) < 8:
        a = "Короткий!"
    elif '123' in pas:
        a = "Простой!"
    elif pas != pas1:
        a = "Различаются."
    else:
        a = "OK"
    print(a)