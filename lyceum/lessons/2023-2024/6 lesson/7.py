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


class OperError(NumberError):
    pass


class CountyError(NumberError):
    pass


try:
    ph = input()
    ph = ph.replace(" ", "").replace("\t", "")
    oper = ['910', '911', '912', '913', '914', '915', '916', '917', '918', '919', '980', '981', '982', '983', '984',
            '985', '986', '987', '988', '989', '920', '921', '922', '923', '924', '925', '926', '927', '928', '929',
            '930', '931', '932', '933', '934', '935', '936', '937', '938', '939', '902', '903', '904', '905', '906',
            '960', '961', '962', '963', '964', '965', '966', '967', '968', '969']
    if ph[:2] == '+7':
        ph = "+7" + ph[2:]
    elif ph[:2] == '+1':
        pass
    elif ph[:3] == '+55':
        pass
    elif ph[:4] == "+359":
        pass
    elif ph[0] == '8':
        ph = "+7" + ph[1:]
    else:
        if ph[0] == '+':
            raise CountyError("не определяется код страны")
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
    if len(ph[1:]) != 11:
        raise LenError("неверное количество цифр")
    if '+7' == ph[:2]:
        if ph[2:5] not in oper:
            raise OperError("не определяется оператор сотовой связи")
    print(ph)
except NumberError as e:
    print(e)
