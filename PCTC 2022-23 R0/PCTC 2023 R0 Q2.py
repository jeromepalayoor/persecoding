mass1=int(input())
vol1 =int(input())
mass2=int(input())
vol2 =int(input())
dens1 = mass1/vol1
dens2 = mass2/vol2
if dens1 > dens2:
    print("1")
elif dens2 > dens1:
    print("2")
else:
    print("same")