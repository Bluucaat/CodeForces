vector_sums = [0, 0, 0]
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    vector_sums[0] += x
    vector_sums[1] += y
    vector_sums[2] += z

print("YES" if vector_sums == [0, 0, 0] else "NO")