from statistics import median as md


def median(data: list):
    if len(data) % 2 == 1:
        return data[len(data) // 2]
    else:
        pivot = len(data) // 2
        return (data[pivot - 1] + data[pivot]) / 2.0


def get_q1(data: list):
    if len(data) % 2 == 1:
        return 0  # data[1:len]


if __name__ == '__main__':
    test = [5, 8, 3, 2, 1, 3, 10, 105]
    test = sorted(test)
    assert median(test) == md(test)

    print('The minimum is: ' + str(test[0]))
    print('The median is: ' + str(median(test)))
    print('The maximum is:' + str(test[-1]))
    input("Aperte Enter para continuar...")
