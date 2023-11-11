import csv


with open('wares.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    sp = []
    for index, row in enumerate(reader):
        if int(row[1]) <= 1000:
            sp.append([row[0], int(row[1])])
if not sp:
    txt = 'error'
else:
    pur, mon = [], 1000
    for item in sorted(sp, key=lambda x: (x[1], x[0])):
        cnt = mon // item[1]
        if cnt > 0:
            pur += [item[0]] * ([cnt, 10][cnt > 10])
            mon -= ([cnt, 10][cnt > 10]) * item[1]
    txt = ', '.join(pur)
with open('output.txt', mode='w', encoding='utf-8') as fp:
    fp.write(txt)