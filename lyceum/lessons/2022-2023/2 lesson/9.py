print("Назовите себя, пожалуйста!")
name = input()
print("Введите текст.")
text = input()
print("Повторите текст.")
text1 = input()
if text == text1:
    print(name + ", введено верно!")
else:
    print(name + ", пока не получилось, попробуйте снова!")