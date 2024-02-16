def polyglots():
    langs: list[str] = []
    langs_map: dict[str, int] = {}
    lang_that_all_knows: list[str] = []
    t: int = int(input("amount of students: "))
    max_amount_of_langs: int = 0

    for _ in range(t):
        n: int = int(input("amount of langs: "))
        is_max: bool = False
        if n > max_amount_of_langs:
            max_amount_of_langs = n
            is_max = True
        for _ in range(n):
            lang: str = input("lang: ")
            if lang not in langs_map:
                langs_map[lang] = 0
            langs_map[lang] += 1

            if is_max:
                langs.append(lang)

    for language in langs_map:
        if langs_map[language] == t:
            lang_that_all_knows.append(language)

    print(len(lang_that_all_knows))
    print(lang_that_all_knows)

    langs.sort()
    print(len(langs))
    print(langs)


polyglots()

# 3
# 3
# English
# Russian
# Japanese
# 2
# Russian
# English
# 1
# English