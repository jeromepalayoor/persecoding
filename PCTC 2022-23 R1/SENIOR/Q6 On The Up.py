f = int(input())
current = f
while 1:
    new = int(input())
    if new > current:
        current = new
    else:
        print(new-f)
        break