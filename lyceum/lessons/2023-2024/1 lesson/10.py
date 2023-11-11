a = input().lower()
b = ''
for i in a:
    if i == 'а':
        b += 'ка'
    elif i == 'б':
        b += 'зу'
    elif i == 'в':
        b += 'ру'
    elif i == 'г':
        b += 'джи'
    elif i == 'д':
        b += 'те'
    elif i == 'е' or i == 'ё':
        b += 'ку'
    elif i == 'ж':
        b += 'зу'
    elif i == 'и':
        b += 'ки'
    elif i == 'й':
        b += 'фу'
    elif i == 'к':
        b += 'ме'
    elif i == 'з':
        b += 'з'
    elif i == 'л':
        b += 'та'
    elif i == 'м':
        b += 'рин'
    elif i == 'н':
        b += 'то'
    elif i == 'о':
        b += 'мо'
    elif i == 'п':
        b += 'но'
    elif i == 'р':
        b += 'ши'
    elif i == 'с':
        b += 'ари'
    elif i == 'т':
        b += 'чи'
    elif i == 'у':
        b += 'мей'
    elif i == 'ф':
        b += 'лу'
    elif i == 'х':
        b += 'ри'
    elif i == 'ц':
        b += 'ми'
    elif i == 'ч':
        b += 'зи'
    elif i == 'ш':
        b += 'ли'
    elif i == 'щ':
        b += 'ни'
    elif i == 'ъ':
        b += 'д'
    elif i == 'ы':
        b += 'хе'
    elif i == 'ь':
        b += 'ксе'
    elif i == 'э':
        b += 'га'
    elif i == 'ю':
        b += 'до'
    elif i == 'я':
        b += 'ма'
a = b.capitalize()
print(a)
