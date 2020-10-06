# -*- coding: utf-8 -*-
import vk_api

# there is only one variable in config.py with group key with access to messages and photos
from config import login, password, access_token
from statisticks import *
from func import *


def main():
    vk_session = vk_api.VkApi(
        login=login, password=password, token=access_token)
    vk = vk_session.get_api()
    world = get_message_from_stat(get_country_stat_or_None('0'))
    rus = get_message_from_stat(get_country_stat_or_None('Россия'))
    usa = get_message_from_stat(get_country_stat_or_None('США'))
    china = get_message_from_stat(get_country_stat_or_None('Китай'))
    msg = f'Мировая статистика по коронавирусу на {get_date()}:\n\n\n{world}\n\n{rus}\n\n{usa}\n\n{china}\n\nНапоминаю, что вы всегда можете написать мне в сообщения, и я пришлю вам статистику!\nВся информация взята с сайта https://www.worldometers.info/coronavirus/'
    vk.wall.post(owner_id=-199225670, from_group=1, message=msg, guid=get_guid())


if __name__ == '__main__':
    main()
