hats    = int(input())
scarves = int(input())
gloves  = int(input())
if not hats:
    if scarves and gloves > 1:
        print('toasty')
        print(scarves-1+gloves-2)
    elif not scarves and gloves > 1:
        print('cold')
        print(gloves-2)
    elif scarves and gloves < 2:
        print('cold')
        print(scarves-1)
    else:
        print('cold')
        print(0)
elif not scarves:
    if hats and gloves > 1:
        print('toasty')
        print(hats-1+gloves-2)
    elif not hats and gloves > 1:
        print('cold')
        print(gloves-2)
    elif hats and gloves < 2:
        print('cold')
        print(hats-1)
    else:
        print('cold')
        print(0)
elif not gloves:
    if hats and scarves:
        print('toasty')
        print(scarves-1+hats-1)
    elif not scarves and hats:
        print('cold')
        print(hats-1)
    elif scarves and not hats:
        print('cold')
        print(scarves-1)
    else:
        print('cold')
        print(0)
else:
    a = 0
    print('toasty')
    print(scarves-1+gloves+hats-1)