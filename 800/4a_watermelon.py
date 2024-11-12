watermelon_weight = int(input("enter watermelon weight: "))
remaining_weight = watermelon_weight-1
found = False
for i in range(2, watermelon_weight - 1):
    remaining_weight-=1
    if (i % 2 == 0) and (remaining_weight % 2 == 0) and (i + remaining_weight) % 2 == 0:
        print("YES")
        found = True
        break

if not found:
    print("NO")
