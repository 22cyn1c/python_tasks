print("Изучаете ли вы программирование?")
answer = input()
print("Читаете ли вы зарубежную литературу?")
answer1 = input()
if answer == "да" and answer1 == "да" :
    print("Да вы гений!")
elif answer == "нет" and answer1 == "да":
    print("Может, это и к лучшему...")
elif answer == "да" and answer1 == "нет":
    print("Продолжайте в том же духе!")
elif answer == "нет" and answer1 == "нет":
    print("Не стоит ли начать?")
else:
    print("Извините, я вас не понимаю")