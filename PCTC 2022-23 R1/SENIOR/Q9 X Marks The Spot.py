x = int(input())
y = int(input())
for i in range(10):
    if i==y:
        print("#"*(x)+"X"+"#"*(10-x-1))
    else:
        print("#"*10)