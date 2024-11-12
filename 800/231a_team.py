num_of_problems = int(input())
num_of_problems_solved = 0
for i in range (num_of_problems):
    line = [int(n) for n in input().split() if int(n) == 1]
    if line.__len__() > 1:
     num_of_problems_solved += 1
print(num_of_problems_solved)

