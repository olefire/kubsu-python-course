def find_dates():
    months = {"января", "февраля", "марта", "апреля", "мая", "июня", "июля",
              "августа", "сентября", "октября", "ноября", "декабря"}

    dates = []
    string = input("input text.txt here: ")
    i = 0
    while i < len(string):
        wp = string.find(" ", i)
        last_index_of_year = i
        if string[i:wp] in months:
            if i != 0 and wp != len(string) - 1 and string[i - 3:i].strip().isdigit() and string[wp + 1].isdigit():
                last_index_of_year = wp + 2
                while last_index_of_year != len(string) and string[last_index_of_year].isdigit():
                    last_index_of_year += 1

                date = string[i-3:last_index_of_year].strip()
                dates.append(date)

        i = last_index_of_year + 1
    return dates


dates = find_dates()
for date in dates:
    print(date)

# "Сегодня 31 февраля 2007 года, а вчера было 15 января 2022 года."