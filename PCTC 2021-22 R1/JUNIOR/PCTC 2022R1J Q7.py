na = 50
no = 50
while na > 0 and no > 0:
    f = input()
    h = int(input())
    if f == 'APPLES':
        na -= h
    else:
        no -= h
print(max(na,no))