for n in range(int(input())):
    input()
    numbers = list(map(int, input().split()))
    for n in range(len(numbers)):
        if numbers.count(numbers[n]) == 1:
            print(n+1)