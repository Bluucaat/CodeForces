string_1, string_2 = input().lower(), input().lower()
if string_1 < string_2:
    print(-1)
elif string_1 == string_2:
    print(0)
else:
    print(1)