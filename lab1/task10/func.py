def organize_by_length():
    n = int(input("input amount of strings: "))
    list = []
    for i in range(n):
        list.append(input())

    list.sort(key=lambda s: len(s.split()))
    print(list)


organize_by_length()
