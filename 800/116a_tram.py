maximum_people_on_train = 0
people_on_train = 0
for i in range(int(input())):
    entry_exit = list(map(int, input().split()))
    people_on_train += entry_exit[1] - entry_exit[0]
    if maximum_people_on_train < people_on_train:
        maximum_people_on_train = people_on_train
print(maximum_people_on_train)