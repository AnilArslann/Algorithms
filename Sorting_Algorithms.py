from turtle import update


def insertion_sort(a):

    updated_list = a

    for step in range(len(a)):
        idx = 0
        min = updated_list[0]

        for number in range(len(updated_list)):

            if updated_list[number] < min:
                min = updated_list[number]
                idx = number
        a[step], a[idx+step] = min, a[step]
        updated_list = a[step+1:]
    return a


def merge_sort(a):
    operated_list = list()
    length_list = int(len(a) / 2)
    for number in range(len(a)):
        operated_list.append([a[number]])

    for step in range(length_list):

        for number2 in range(0, len(operated_list)-1, 2):

            arbitrary = list()

            x = 0
            y = 0
            print(number2)
            while x < len(operated_list[number2]) and y < len(operated_list[number2 + 1]):

                if operated_list[number2][x] < operated_list[number2 + 1][y]:
                    arbitrary.append(operated_list[number2][x])
                    x += 1
                else:
                    arbitrary.append(operated_list[number2 + 1][y])
                    y += 1

            operated_list[number2] = arbitrary
            operated_list[number2 + 1] = "a"
            print(operated_list)
        for z in range(len(operated_list)):

            if operated_list[z] == "a":
                operated_list.remove("a")


merge_sort([4, 5, 3, 2, 6])
print("hello")
