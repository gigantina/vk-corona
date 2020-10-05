from random import randint
from statisticks import data


def get_random_id():
    res = randint(0, 1000000000)
    return res


def get_message_from_tuple(tuple_):
    stat, n = tuple_[0], tuple_[1]
    res = ''
    for i in range(14):
        part_of_stat = data[i]
        res += f'{part_of_stat}: {stat[part_of_stat]}\n'
    return res
