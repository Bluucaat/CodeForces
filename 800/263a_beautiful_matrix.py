input_matrix = []
index_of_one = (-1, -1)
middle = 2

for i in range(5):
    row = list(map(int, input().split(" ")))
    input_matrix.append(row)
    if 1 in input_matrix[i]:
        index_of_one = (i, input_matrix[i].index(1))

distance_tuple = tuple(abs(x - middle) for x in index_of_one)
print(distance_tuple[0] + distance_tuple[1])