n = int(input())
x = 0
s = 0
while n > 4:
    n -= 5
    x += 5
    s += x
x += n
s += x
print(s)
