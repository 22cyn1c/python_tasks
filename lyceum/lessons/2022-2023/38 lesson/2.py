def cutting_spot(*n):
    a = {"2": [], "3": [], "5": []}
    b = 'ёйцукенгшщзхъфывапролджэячсмитьбюqwertyuiopaasdfghjklzxcvbnm'
    d = ''
    for i in n:
        if len(i) % 5 == 0:
            a["5"].append(i.lower().capitalize())
        if len(i) % 3 == 0:
            a["3"].append(i.lower())
        if len(i) % 2 == 0:
            for j in range(len(i)):
                if i[j] in b:
                    d += i[j].upper()
                else:
                    d += i[j].lower()
            a["2"].append(d)
            d = ''
    a["5"].sort()
    a["3"].sort()
    a["2"].sort()
    return a