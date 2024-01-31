v = 0
for _ in range(12):
    x = input()
    if abs(int(x[0])-int(x[-1])) == 1:
        v += 1
print(v)