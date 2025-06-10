vowels = ['a', 'e', 'i', 'o', 'u', 'y']
new_str = ""
for char in input().lower():
    if char not in vowels:
        new_str += '.' + char
print(new_str)