import sys


co = 0
for i in sys.stdin:
    if 'далек' in i.lower():
        co += 1
print(co)