a = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n", "г": "g", "ш": "sh", "щ": "shh",
     "з": "z", "х": "h", "ъ": "#", "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
     "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya", "ч": "ch", "с": "s", "м": "m",
     "и": "i", "т": "t", "ь": "'", "б": "b", "ю": "ju", "ё": "jo"}

with open('cyrillic.txt', encoding='utf-8') as f:
    fwrite = open('transliteration.txt', 'w')
    for s in f.read():
        if s.lower() in a:
            if s.isupper():
                fwrite.write(a[s.lower()].capitalize())
            else:
                fwrite.write(a[s.lower()])
        else:
            fwrite.write(s)
    fwrite.close()