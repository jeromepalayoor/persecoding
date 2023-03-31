pay = int(input())
sells = int(input())
if sells > 10:
    pay += 60
elif sells > 8:
    pay += 40
elif sells > 5:
    pay += 20
print(pay)