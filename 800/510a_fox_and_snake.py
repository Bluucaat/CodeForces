size = list(map(int, input().split(" ")))
rows, cols = size[0], size[1]

snake = [["#" if row % 2 == 0 else "." for _ in range(cols)] for row in range(rows)]
step = 0
for i in range(rows):
    if i % 2 != 0:
        if step == 0:
            snake[i][cols - 1] = "#"
            step = 1
        elif step == 1:
            snake[i][0] = "#"
            step = 0
for row in snake:
    print("".join(row))
