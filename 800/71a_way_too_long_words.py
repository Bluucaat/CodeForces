word_count = int(input())
for i in range(word_count):
    word = input()
    if len(word) <= 10:
        print(word)
    else:
        print(f"{word[0]}{len(word[1:-1])}{word[-1]}")

