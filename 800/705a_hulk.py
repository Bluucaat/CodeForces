layers = int(input())
answer = ""
for i in range(layers):
    if i == layers - 1 and i % 2 == 0:
        answer += " I hate it"
    elif i == layers - 1 and i % 2 == 1:
        answer += " I love it"
    else:
        if i % 2 == 0:
            answer += (" I hate that")
        else:
            answer += (" I love that")
print(answer.lstrip())
