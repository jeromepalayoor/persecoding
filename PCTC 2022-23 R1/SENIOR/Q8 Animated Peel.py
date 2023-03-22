word = input()
length = len(word)
for i in range(length//2):
    new = word[length//2-1]
    new += word[0:length//2-1]
    new += word[length//2+1:length]
    new += word[length//2]
    word = new
    print(new)