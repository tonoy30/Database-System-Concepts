from random import randint


def gen_random(n):
    start_range = 10 ** (n-1)
    end_range = (10 ** n) - 1
    return randint(start_range, end_range)
