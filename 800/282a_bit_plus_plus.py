amount_of_operations = int(input())
int
ans = 0;
for i in range(amount_of_operations):
    operation = input()
    if operation == "++X" or operation == "X++":
        ans += 1
    elif operation == "--X" or operation == "X--":
        ans -= 1

print(ans)