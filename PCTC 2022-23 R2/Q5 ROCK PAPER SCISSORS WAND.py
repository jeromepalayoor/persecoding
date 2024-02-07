score = [0, 0]
a_win = ['SP', 'RS', 'PR', 'WR', 'WS', 'WP']
b_win = ['PS', 'SR', 'RP', 'RW', 'SW', 'PW']
a_rec = -1

for _ in range(6):
    x = input()
    if x in a_win:
        score[0] += 1
        if x[0] == 'W':
            a_rec = 1
    elif x in b_win:
        score[1] += 1
        if x[1] == 'W':
            a_rec = 0
    else:
        if x == 'WW':
            if a_rec == 1:
                score[0] = 0
            elif a_rec == 0:
                score[1] = 0
print(f'{score[0]}-{score[1]}')