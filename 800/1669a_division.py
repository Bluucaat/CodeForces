test_case_count = int(input())
for i in range(test_case_count):
    user_score = int(input())
    if user_score >= 1900: print("Division 1")
    elif 1600 <= user_score <= 1899: print("Division 2")
    elif 1400 <= user_score <= 1599: print("Division 3")
    else: print("Division 4")