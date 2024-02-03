def count_of_russian_letters():
    text = input("input text here: ")
    letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    count = 0
    for letter in text:
        if letter.lower() in letters:
            count += 1
    print(count)

