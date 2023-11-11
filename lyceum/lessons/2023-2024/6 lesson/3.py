class NumberError(Exception):
    pass


class BeginError(NumberError):
    pass


class BracketError(NumberError):
    pass


class DashError(NumberError):
    pass


class LenError(NumberError):
    pass


class FormatError(NumberError):
    pass


# ph = input()
# ph = ph.replace(" ", "").replace("\t", "")
# if ph[:1] == '+7':
#     ph = "+7" + ph[2:]
# elif ph[0] == '8':
#     ph = "+7" + ph[1:]
# else:
#     raise BeginError('Неверное начало номера!')
# if "(" in ph and ")" in ph:
#     ph = ph[:ph.index("(")] + ph[ph.index("(") + 1:ph.index(")")] + ph[ph.index(")") + 1:]
# else:
#     raise BracketError('Больше одной пары скобок!')
# if "--" not in ph and "-" in ph:
#     ph = ph[0] + ph[1:-1].replace("-", "") + ph[-1]
# else:
#     raise DashError('Подряд идущие тире!')
# if not ph[1:].isdigit() or len(ph[1:]) != 11:
#     raise LenError('Неверное количество цифр!')
try:
    ph = input()
    ph = ph.replace(" ", "").replace("\t", "")
    if ph[:2] == '+7':
        ph = "+7" + ph[2:]
    elif ph[0] == '8':
        ph = "+7" + ph[1:]
    else:
        raise BeginError("неверный формат")
    if "(" in ph or ")" in ph:
        if "(" in ph and ")" in ph:
            ph = ph[:ph.index("(")] + ph[ph.index("(") + 1:ph.index(")")] + ph[ph.index(")") + 1:]
        else:
            raise BracketError("неверный формат")
    if "-" in ph:
        if "--" not in ph and "-" in ph:
            ph = ph[0] + ph[1:-1].replace("-", "") + ph[-1]
        else:
            raise DashError("неверный формат")
    if not ph[1:].isdigit():
        raise FormatError('неверный формат')
    if len(ph[1:]) == 11:
        print(ph)
    else:
        raise LenError("неверное количество цифр")
except NumberError as e:
    print(e)
