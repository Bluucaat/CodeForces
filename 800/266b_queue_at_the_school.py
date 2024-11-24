time = int(input().split()[1])
queue = list(input())

for _ in range(time):
    i = 0
    while i < len(queue) - 1:
        if queue[i] == "B" and queue[i + 1] == "G":
            queue[i], queue[i + 1] = queue[i + 1], queue[i]
            i += 1
        i += 1

print("".join(queue))
