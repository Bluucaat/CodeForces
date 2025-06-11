def is_lucky(n):
    return all(ch in '47' for ch in str(n))

def generate_lucky_numbers(limit):
    result = []

    def dfs(current):
        if current:
            num = int(current)
            if num > limit:
                return
            result.append(num)
        dfs(current + '4')
        dfs(current + '7')

    dfs("")
    return result

n = int(input())

if is_lucky(n):
    print("YES")
else:
    for lucky in generate_lucky_numbers(n):
        if n % lucky == 0:
            print("YES")
            break
    else:
        print("NO")