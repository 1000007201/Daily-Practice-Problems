list_ = [1, 5, 8, 12, 3, 17, 13]


def get_max(arr, max):
    arr.sort()
    return arr[-max]


if __name__ == "__main__":
    out_max = get_max(list_, 3)
    print(out_max)