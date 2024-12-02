level_amount = int(input())
solved_level_set = (set(map(int, input().split()[1::]))
                    .union(set(map(int, input().split()[1::]))))
if 0 in solved_level_set: solved_level_set.remove(0)
if len(solved_level_set) == level_amount:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")