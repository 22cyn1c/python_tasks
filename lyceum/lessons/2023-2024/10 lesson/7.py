import csv


with open('wares.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index:
            if int(row[1]) > int(row[2]):
                print(row[0])