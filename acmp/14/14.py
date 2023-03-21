'''
https://acmp.ru/index.asp?main=task&id_task=14
'''
import math


a, b = map(int,input().split())
print(int(a * b / math.gcd(a, b)))