input_data = list(map(int, input().split()))
n, k, l, c, d, p, nl, np = input_data

toasts_by_drinks = ((k * l) // nl) // n
toasts_by_limes = (c * d) // n
toasts_by_salt = (p // np) // n

print(min(toasts_by_drinks, toasts_by_limes, toasts_by_salt))
