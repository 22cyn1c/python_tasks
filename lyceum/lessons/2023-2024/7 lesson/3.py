def reverse():
    with open('input.dat', mode='rb') as fr:
        sp = fr.read()
    with open('output.dat', mode='wb') as fw:
        fw.write(sp[::-1])