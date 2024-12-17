coords = sorted(list(map(int, input().split())))
print(coords[2]-coords[1] + coords[1] - coords[0])