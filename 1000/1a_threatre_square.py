input_params = list(map(int, input().split()))
square_size = input_params[2]
count = ((input_params[0] + square_size - 1) // square_size) * ((input_params[1] + square_size - 1) // square_size)
print(count)