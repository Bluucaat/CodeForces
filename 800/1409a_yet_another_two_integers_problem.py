for n in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        print(0)
    else:
        print(abs(a-b)//10 + (abs(a-b) % 10 > 0))
