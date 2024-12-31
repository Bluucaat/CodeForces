input()
performances = list(map(int, input().split()))
curr_min = performances[0]
curr_max = performances[0]
amazing_count = 0
for n in range(1, len(performances)):
    if performances[n] < curr_min:
        amazing_count += 1
        curr_min = performances[n]
    elif performances[n] > curr_max:
        amazing_count += 1
        curr_max = performances[n]
print(amazing_count)
