# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import requests
from translate import Translator

global data
data = ['Страна', 'Всего случаев', 'Новые случаи', 'Всего смертей', 'Новых смертей', 'Всего выздоровело',
        'Новых выздоровело', 'Активные случаи', 'Критические случаи', 'Случаи на 1 млн человек',
        'Смертей на 1 млн человек', 'Всего тестов', 'Тестов на 1 млн человек', 'Количество населения']


def get_statistics():
    url = 'https://www.worldometers.info/coronavirus/'

    html = requests.get(url).text
    soup = bs(html, 'lxml')
    table = soup.find('tbody').text

    stat = {}

    stat['0'] = {}
    world = table[table.find('World'):].split('\n')[:11]
    for i in range(14):
        if i < 11:
            stat['0'][data[i]] = world[i]
        else:
            stat['0'][data[i]] = 'N/A'
    table = table[table.find('All') + 10:].split('\n')


    flag = False
    none = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Australia/Oceania']
    changed_table = []

    for i in range(len(table)):
        if table[i] in none:
            flag = True
        elif flag:
            flag = False

        else:
            if i < len(table) - 3:
                if table[i + 4] == 'Anguilla' or table[i + 3] == 'Anguilla': # still a crutch
                    continue
                else:
                    changed_table.append(table[i])

    dp = changed_table.index('Diamond Princess')

    changed_table = changed_table[:dp - 1] + changed_table[dp + 18:]
    for i in range(len(changed_table)):
        n = i % 17
        if n == 0:
            active_country = changed_table[i]
            stat[active_country] = {}
        elif n < 15:
            stat[active_country][data[n - 1]] = changed_table[i]
    return stat


def get_country_stat_or_None(query):
    lang = 'russian'
    res = None
    try:
        if query.isalpha():
            translator = Translator(from_lang=lang, to_lang='english')
            query = translator.translate(query)
        stat = get_statistics()
        for i in range(len(stat) + 1):
            if str(i) in stat:
                if stat[str(i)]['Страна'] == query or str(i) == query:
                    res = stat[str(i)]
    except Exception as e:
        print(e)
    return res