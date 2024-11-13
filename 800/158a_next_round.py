n, k = map(int, input().split())
results = list(map(int, input().split()))
pass_score = results[k-1]
i = 0
for r in results:
    if r >= pass_score and r > 0:
        i += 1
print(i)