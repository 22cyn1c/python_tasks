ph = input()
ph = ph.replace(" ", "").replace("\t", "")
if ph[:1] == '+7':
    ph = "+7" + ph[2:]
elif ph[0] == '8':
    ph = "+7" + ph[1:]
if "(" in ph and ")" in ph:
    ph = ph[:ph.index("(")] + ph[ph.index("(") + 1:ph.index(")")] + ph[ph.index(")") + 1:]
if "--" not in ph and "-" in ph:
    ph = ph[0] + ph[1:-1].replace("-", "") + ph[-1]
if ph[1:].isdigit() and len(ph[1:]) == 11:
    print(ph)
else:
    print("error")