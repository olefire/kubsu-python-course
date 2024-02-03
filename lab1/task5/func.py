def find_dates():
    months = {
        "января": 1,
        "февраля": 2,
        "марта": 3,
        "апреля": 4,
        "мая": 5,
        "июня": 6,
        "июля": 7,
        "августа": 8,
        "сентября": 9,
        "октября": 10,
        "ноября": 11,
        "декабря": 12
    }

    dates = []
    words = input().split()
    for i in range(len(words) - 2):
        if words[i].isdigit() and words[i + 1] in months and words[i + 2].isdigit():
            date = ' '.join(words[i:i+3])
            dates.append(date)
    return dates


dates = find_dates()
for date in dates:
    print(date)
