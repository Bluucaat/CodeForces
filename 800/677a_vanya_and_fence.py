min_road_width = 0
fence_height = int(input().split(" ")[1])
for friend in map(int, input().split(" ")):
    if friend > fence_height:
        min_road_width += 2
    else:
        min_road_width += 1
print(min_road_width)