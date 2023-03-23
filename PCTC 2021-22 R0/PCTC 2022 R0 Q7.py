sum = 0
burgor = input()
if burgor == "lettuce" or burgor == "carrot":
    sum += 50
    ketchup = input()
    if ketchup == "y":
        sum += 15
else:
    sum += 70
howmany = int(input())
if 0 <= howmany <= 5:
    sum += howmany*5
print(sum)