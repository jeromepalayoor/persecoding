while 1:
    x = input()
    a, b = x.split(' ')
    if a == b:
        continue
    else:
        if len(a) < len(b):
            a += '_'*(len(b)-len(a))
        else:
            b += '_'*(len(a)-len(b))
        for i in range(len(a)):
            if a[i] != b[i]:
                print(a[i], b[i])
                exit()