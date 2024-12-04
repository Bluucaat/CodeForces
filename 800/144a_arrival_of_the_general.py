input()
line_up = list(map(int, input().split()))

index_of_max = line_up.index(max(line_up))
index_of_min = len(line_up) - 1 - line_up[::-1].index(min(line_up))

if index_of_max < index_of_min:
    print(index_of_max + (len(line_up) - 1 - index_of_min))
else:
    print(index_of_max + (len(line_up) - 1 - index_of_min) - 1)
