# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

m, n = map(int, input().split())
magazine = list(input().split())
note = list(input().split())

magazine_word_freq = {}

for word in magazine:
    if word not in magazine_word_freq:
        magazine_word_freq[word] = 0
    magazine_word_freq[word] += 1

for word in note:
    if word in magazine and magazine_word_freq[word] > 0:
        magazine_word_freq[word] -= 1
        continue
    else:
        print('No')
        break
else:
    print('Yes')
