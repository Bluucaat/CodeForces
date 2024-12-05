hurt_count = 0
numbers = set(int(input()) for _ in range(4))
dragon_amount = int(input())
for i in range(1, dragon_amount+1):
    for n in numbers:
        if i % n == 0:
            hurt_count += 1
            break
print(hurt_count)
