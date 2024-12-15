summable = []
ans = ""

for i in range(int(input())):
    n = list(map(int, input()))[::-1]
    summable.clear()
    rev_index = 1
    for digit in n:
        if not (digit % 10 == 0):
            summable.append(digit * rev_index)
        rev_index *= 10
    ans += f"{len(summable)}\n{' '.join(map(str, summable))}\n"
print(ans)
