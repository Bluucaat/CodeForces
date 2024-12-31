input_params = list(map(int, input().split()))
n, travel_time = input_params[0], input_params[1]
time = 240 - travel_time
problem_index = 1
while problem_index <= n and time >= (5 * problem_index):
    time -= (5 * problem_index)
    problem_index += 1
print(problem_index-1)