grid = [[f'{i:02}' for i in range(j*10, (j+1)*10)] for j in range(10)]

for _ in range(int(input())):
    x = input()
    if x[0] == 'r':
        a, b = map(int, x[1:].split('-'))
        grid = grid[:min(a, len(grid))] + grid[min(b+1, len(grid)):]
    else:
        a, b = map(int, x[1:].split('-'))
        for i in range(len(grid)):
            grid[i] = grid[i][:min(a, len(grid[i]))] + grid[i][min(b+1, len(grid[i])):]

for i in grid:
    print(' '.join(i))