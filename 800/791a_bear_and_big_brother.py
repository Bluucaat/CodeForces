weight_a, weight_b = map(int, input().split(" "))
for year in range(20):
    if weight_a>weight_b:
        print(year)
        break
    weight_a *= 3
    weight_b *= 2