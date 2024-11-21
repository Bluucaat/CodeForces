word_to_translate = input()
translated_word = input()
if translated_word == word_to_translate[::-1]:
    print("YES")
else:
    print("NO")