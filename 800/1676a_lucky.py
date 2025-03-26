for n in range(int(input())):
    print("YES" if (lambda s: sum(s[:(len(s)//2)]) == sum(s[(len(s)//2):]))(list(map(int, input()))) else "NO")
