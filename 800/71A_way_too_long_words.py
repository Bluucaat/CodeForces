word_count = int(input())
for i in range(word_count):
    word = input()
    if word.__len__() <= 10:
        print(word)
    else:
        print(f"{word[0]}{len(word[1:-1])}{word[-1]}")

