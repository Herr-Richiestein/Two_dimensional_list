import random


def pick_sample(sample):
    c = random.choices(sample, 3)
    return c


def main():
    m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    print(pick_sample(m))


main()