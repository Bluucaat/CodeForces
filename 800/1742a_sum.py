def is_sum_of_other_two(a, b, c):
    return a+b == c or a+c == b or b+c == a

for i in range(int(input())):
    nums = (list(map(int, input().split())))
    if is_sum_of_other_two(*nums):
        print("YES")
    else:
        print("NO")