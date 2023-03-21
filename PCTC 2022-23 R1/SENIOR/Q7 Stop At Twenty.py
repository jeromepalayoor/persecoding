total = 0
numbers = 0
for i in range(100):
    a = int(input())
    numbers += 1
    if a + total > 20:
        total = 0
    elif a + total < 20:
        total += a
    else:
        print(numbers)
        break