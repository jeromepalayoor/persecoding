temp = input()
lap = int(input())*2
if temp == 'warm' and lap <= 10:
    lap *= 3/2
print(int(lap))