grid = [list(input()) for _ in range(6)]
for i in range(6):
    for j in range(6):
        if grid[i][j] == '#':
            x, y = i, j
            break
prevx = -1
prevy = -1
while True:
    if (prevx, prevy) == (x, y):
        grid[x][y] = '#'
        break
    if grid[(x-1)%6][y] == '0' and prevx != (x-1)%6:
        prevx, prevy = x, y
        x = (x-1)%6
    elif grid[x][y-1] == '0' and prevy != (y-1)%6:
        prevx, prevy = x, y
        y = (y-1)%6
    elif grid[x][(y+1)%6] == '0' and prevy != (y+1)%6:
        prevx, prevy = x, y
        y = (y+1)%6
    elif grid[(x+1)%6][y] == '0' and prevx != (x+1)%6:
        prevx, prevy = x, y
        x = (x+1)%6
    else:
        break
    # print()
    # for row in grid:
    #     print(''.join(row))
    
    grid[prevx][prevy] = '0'
    grid[x][y] = '#'
for row in grid:
    print(''.join(row))