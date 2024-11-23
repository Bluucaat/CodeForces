current_beautiful_year = int(input())

for i in range(current_beautiful_year + 1, 10000):
    digits_set = {int(digit) for digit in str(i)}
    if len(digits_set) == 4:
        print(i)
        break