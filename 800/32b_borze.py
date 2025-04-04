expression = input()
result_string = ""
i = 0
while i < len(expression):
    if expression[i] == '.':
        result_string += "0"
        i+=1
    elif expression[i] == '-':
        if expression[i+1] == '.':
            result_string += "1"
        elif expression[i+1] == '-':
            result_string += "2"
        i += 2

print(result_string)
