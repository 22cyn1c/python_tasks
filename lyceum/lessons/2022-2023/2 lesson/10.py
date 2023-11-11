login = input()
mail = input()
if "@" not in login and "@" in mail:
    print("OK")
elif "@" in login:
    print("Некорректный логин")
elif "@" not in mail:
    print("Некорректный адрес")