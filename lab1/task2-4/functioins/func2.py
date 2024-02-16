def find_count_of_words_with_even_count_of_letters():
    words = input().split()
    count = 0
    for word in words:
        if len(word) % 2 == 0:
            count += 1
    print("количество слов с четным количеством символов", count)