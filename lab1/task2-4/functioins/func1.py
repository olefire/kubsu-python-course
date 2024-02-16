from random import randint


def mix_words():
    words = input().split()
    for i in range(len(words)):
        j = randint(0, len(words) - 1)
        temp = words[i]
        words[i] = words[j]
        words[j] = temp

    for word in words:
        print(word)
