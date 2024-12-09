team_count = int(input())
colors = [input().split() for _ in range(team_count)]
count = 0
for i in range(team_count -1):
    for y in range(i, team_count):
        if i != y:
            if colors[i][0] == colors[y][1] and colors[i][1] == colors[y][0]:
                count+=1
            if colors[i][0] == colors[y][1] or colors[i][1] == colors[y][0]:
                count+=1
print(count)