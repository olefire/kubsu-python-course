from random import randint


def organize_flag():
    def mix_array(arr):
        for i in range(len(arr)):
            j = randint(0, len(arr) - 1)
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    colors = ["white", "blue", "red"]
    mix_array(colors)
    print("original list: ", colors)

    for i, color in enumerate(["white", "blue"]):
        index = colors.index(color)
        colors[index] = colors[i]
        colors[i] = color

    print("organized list: ", colors)


