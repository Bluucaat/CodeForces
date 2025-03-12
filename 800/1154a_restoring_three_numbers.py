sums = list(map(int, input().split()))
sum_of_all = sums.pop(sums.index(max(sums)))
print(" ".join(str(sum_of_all - n) for n in sums))

