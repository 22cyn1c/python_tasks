a = input()
b = input()
if "Тула" in a and "Тула" not in b and "Пенза" not in b:
    print("ДА")
elif 'Пенза' in b and "Тула" not in a and "Пенза" not in a:
    print("ДА")
else:
    print("НЕТ")