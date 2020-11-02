import vk_api
import random
import time
import sys
from vk_api.longpoll import VkLongPoll, VkEventType

id_of_gay = [606626665, 458050531]
'''
gay_msgs = ['а ты таблетки принял?', 'бомбануло', 'ненужно', 'bloated', 'на винфак!', 'угаманись хахлинка',
            'опять троллишь', 'удали', 'хрюкни еще что-нибудь', 'в палату, шизоид!', 'мелкомягких не спрашивали']
'''
gay_msgs = ['а ты таблетки принял?', 'бомбануло', 'угаманись хахлинка',
            'опять троллишь', 'удали', 'хрюкни еще что-нибудь', 'в палату, шизоид!', 'Не хрюкать!!', 'хохла спросить забыли']

vk_session = vk_api.VkApi(token=sys.argv[1])
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and hasattr(event, 'chat_id'):
        try:
            if event.user_id in id_of_gay:
                vk.messages.send(chat_id=event.chat_id,
                                 message=random.choice(gay_msgs),
                                 reply_to=event.message_id,
                                 random_id=random.randint(1, 999999))
        except KeyError:
            pass
        time.sleep(4)
