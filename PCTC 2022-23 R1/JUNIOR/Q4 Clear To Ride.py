age = int(input())
if age < 8 and age >= 6:
    if input() == "Y":
        print("A")
    else:
        print("N")
elif age >= 8 and age < 10:
    print("A")
elif age >= 10:
    print("B")
else:
    print("N")