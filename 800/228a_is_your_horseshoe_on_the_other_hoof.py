horseshoes_list = list(map(int, input().split()))
horseshoes_set = set(horseshoes_list)
print(len(horseshoes_list) - len(horseshoes_set))