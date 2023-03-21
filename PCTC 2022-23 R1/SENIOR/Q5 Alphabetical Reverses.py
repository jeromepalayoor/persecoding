a = input()
b = ''.join(reversed(a))
if a[0] < b[0]:
    print(a)
    print(b)
else:
    print(b)
    print(a)