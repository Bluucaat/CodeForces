for i in range(int(input())):
    input()
    numbers = sorted(map(int, input().split()))
    possible_to_obtain = True
    for i in range(len(numbers)-1):
        if numbers[i+1] - numbers[i] > 1:
            possible_to_obtain = False
            break
    print("YES" if possible_to_obtain else "NO")
