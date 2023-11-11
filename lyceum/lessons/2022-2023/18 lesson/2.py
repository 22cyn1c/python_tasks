a = input().lower()
a = a.split()
c = []
for i in a:
    for e in i:
        if e == 'a':
            c.append('.-')
        if e == 'b':
            c.append('-...')
        if e == 'c':
            c.append('-.-.')
        if e == 'd':
            c.append('-..')
        if e == 'e':
            c.append('.')
        if e == 'f':
            c.append('..-.')
        if e == 'g':
            c.append('--.')
        if e == 'h':
            c.append('....')
        if e == 'i':
            c.append('..')
        if e == 'j':
            c.append('.---')
        if e == 'k':
            c.append('-.-')
        if e == 'l':
            c.append('.-..')
        if e == 'm':
            c.append('--')
        if e == 'n':
            c.append('-.')
        if e == 'o':
            c.append('---')
        if e == 'p':
            c.append('.--.')
        if e == 'q':
            c.append('--.-')
        if e == 'r':
            c.append('.-.')
        if e == 's':
            c.append('...')
        if e == 't':
            c.append('-')
        if e == 'u':
            c.append('..-')
        if e == 'v':
            c.append('...-')
        if e == 'w':
            c.append('.--')
        if e == 'x':
            c.append('-..-')
        if e == 'y':
            c.append('-.--')
        if e == 'z':
            c.append('--..')
    print(*c)
    c = []