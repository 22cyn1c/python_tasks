import csv


procent = float(input())
with open('vps.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index:
            digits = list(map(float, row[1:]))
            if digits[-2] >= procent:
                print(row[0])