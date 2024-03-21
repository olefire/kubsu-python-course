def count_of_latin_lower_letters():
    text = input("input text.txt here: ")
    letters = "abcdefghijklmnopqrstuvwxyz"
    used_letters = set()
    for letter in text:
        if letter in letters:
            used_letters.add(letter)

    print(used_letters)

