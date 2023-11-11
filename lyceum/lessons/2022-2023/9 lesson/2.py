n = input()
ns1 = set()
ns2 = set()
while n != '':
    ns1.add(n)
    n = input()
n = input()
while n != '':
    ns2.add(n)
    if n != '':
        n = input()
ns3 = ns1 & ns2
if ns3 != set():
    for elem in ns3:
        print(elem)
else:
    print('EMPTY')