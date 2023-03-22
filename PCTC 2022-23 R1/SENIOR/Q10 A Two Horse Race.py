a = "|..........|"
h0 = 0
h1 = 0
done = None
for i in range(22):
    h1h0 = int(input())
    if h1h0 and not done:
        h1+=1
    elif not h1h0 and not done:
        h0+=1
    if (h0==11 or h1==11) and not done:
        done = True

ah0 = a[:h0] + "H" + a[h0+1:]
ah1 = a[:h1] + "H" + a[h1+1:]
print(ah0)
print(ah1)