sums = (list(map(int, input().split())))
sums.sort()
if sums[0] == sums[1] == sums[2]:
    num = sums[3]-sums[0]
    print(num, num, num, sep=" ")
else:
    print(sums[3]-sums[2], sums[3]-sums[1], sums[3]-sums[0], sep=" ")

