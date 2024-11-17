word = input()
sum_upper_case = len([i for i in word if ord(i) <= 90])
if sum_upper_case > len(word)/2:
 print(word.upper())
else:
    print(word.lower())