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

    for number in range(len(a)):
        operated_list.append([a[number]])

    while len(operated_list) > 1:

        number2 = 1

        while number2 < len(operated_list):
            arbitrary = list()
            for i in range(len(operated_list[number2])+len(operated_list[number2-1])):
                arbitrary.append(0)

            idx = 0
            while len(operated_list[number2]) > 0 or len(operated_list[number2-1]) > 0:

                if len(operated_list[number2]) > 0 and len(operated_list[number2-1]) > 0:
                    if operated_list[number2][0] > operated_list[number2-1][0]:
                        arbitrary[idx] = operated_list[number2-1][0]
                        operated_list[number2 -
                                      1].remove(operated_list[number2-1][0])

                    else:
                        arbitrary[idx] = operated_list[number2][0]
                        operated_list[number2].remove(
                            operated_list[number2][0])

                elif len(operated_list[number2]) > 0 and not len(operated_list[number2-1]) > 0:
                    arbitrary[idx] = operated_list[number2][0]

                    operated_list[number2].remove(operated_list[number2][0])
                else:
                    arbitrary[idx] = operated_list[number2-1][0]

                    operated_list[number2 -
                                  1].remove(operated_list[number2-1][0])
                idx += 1
            operated_list[number2] = arbitrary

            number2 += 2
        for z in operated_list:
            if len(z) == 0:
                operated_list.remove(z)
    return operated_list[0]


def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a.pop()
    greater = list()
    lesser = list()
    for i in a:
        if i <= pivot:
            lesser.append(i)
        else:
            greater.append(i)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)
