def get_domino_count(m, n):
    if m < 0 or n < 0:
        return 0

    if ((m and n % 2 == 1) or (m or n == 1)
            or (m * n % 2 == 0)):
        return m * n // 2
    elif m % 2 == 0:
        return (m * (n - 1)) // 2 + n // 2
    elif n % 2 == 0:
        return ((m - 1) * n) // 2 + m // 2

m, n = map(int, input().split(" "))
print(get_domino_count(m, n))
