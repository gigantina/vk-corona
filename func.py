from random import randint, shuffle
from statisticks import data
import datetime


def get_random_id():
    res = randint(0, 1000000000)
    return res


def get_message_from_stat(stat):
    res = ''
    for i in range(14):
        part_of_stat = data[i]
        res += f'{part_of_stat}: {stat[part_of_stat]}\n'
    return res

def get_date():
    now = datetime.datetime.now()
    res = now.strftime('%d.%m.%Y')
    return res

def get_guid():
    symb = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@&')
    shuffle(symb)
    return ''.join(symb[:randint(15, 20)])

