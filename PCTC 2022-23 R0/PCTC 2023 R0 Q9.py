a = ['0','0','0','0','0']
for i in range(5):
    c = input()
    a[int(c[0])-1] = c[1]
print("".join(a))