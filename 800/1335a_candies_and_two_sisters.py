test_cases = int(input())
for i in range(test_cases):
    num = int(input())
    if num < 2:
        print(0)
    elif num % 2 == 0:
        print((num // 2)- 1)
    elif num % 2 == 1:
        print(num // 2)