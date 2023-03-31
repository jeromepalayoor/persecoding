pin = input()
for p in range(3):
    if pin[p] >= pin[p+1]:
        print(pin[p+1])