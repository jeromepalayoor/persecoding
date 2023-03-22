size = int(input())
if size%5==0:
    print(f'{size//5}x5')
elif size%4==0:
    print(f'{size//4}x4')
elif size%3==0:
    print(f'{size//3}x3')