s = input()
wordToCheck = 'hello'
wordIndex = 0

for ch in s:
    if ch == wordToCheck[wordIndex]:
        wordIndex += 1
        if wordIndex == len(wordToCheck):
            break

if wordIndex == len(wordToCheck):
    print('YES')
else:
    print('NO')