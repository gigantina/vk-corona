import vk_api

from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
# there is only one variable in config.py with group key with access to messages and photos
from config import TOKEN
from statisticks import *
from func import *


def main():
    url = 'стопкоронавирус.рф/information'
    vk_session = vk_api.VkApi(
        token=TOKEN)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    keyboard = VkKeyboard(one_time=True)

    keyboard.add_button('Мир', color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button('США', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Россия', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Индия', color=VkKeyboardColor.SECONDARY)

    keyboard.add_line()
    keyboard.add_button('Помощь', color=VkKeyboardColor.PRIMARY)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.text == "Начать" or event.text == "Помощь":
                vk.messages.send(
                    user_id=event.user_id,
                    message='Привет, я создан для отображения статистики коронавируса по странам! Чтобы использовать меня, напиши любую страну или число - место по заболеваемости. Попробую все найти!',
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard()
                )
            else:
                stat = get_country_stat_or_None(event.text)
                if stat:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=get_message_from_tuple(stat),
                        random_id=get_random_id(),
                        keyboard=keyboard.get_keyboard()
                    )
                else:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=f'По запросу "{event.text}" ничего не найдено! Попробуйте изменить запрос. Напоминаю, что вы можете ввести число - место страны в списке по заболеваемости или название страны, про которую хотите узнать',
                        random_id=get_random_id(),
                        keyboard=keyboard.get_keyboard()
                    )


if __name__ == '__main__':
    main()
