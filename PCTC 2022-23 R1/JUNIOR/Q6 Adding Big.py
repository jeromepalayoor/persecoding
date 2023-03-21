numbers = []
for i in range(5):
    numbers.append(int(input()))
sum = 0
for x in numbers:
    if x >= 100:
        sum += x
print(sum)