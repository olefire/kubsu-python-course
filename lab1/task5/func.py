def find_dates():
    months = {"января", "февраля", "марта", "апреля", "мая", "июня", "июля",
              "августа", "сентября", "октября", "ноября", "декабря"}

    dates = []
    words = input("input text here: ").split()
    for i in range(len(words) - 2):
        if words[i].isdigit() and words[i + 1] in months and words[i + 2].isdigit():
            date = ' '.join(words[i:i+3])
            dates.append(date)
    return dates


dates = find_dates()
for date in dates:
    print(date)
