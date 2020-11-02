import vk_api
import random
import sys
from vk_api.longpoll import VkLongPoll, VkEventType

id_of_gay = [1]

try:
    with open('messages.txt', 'r') as f:
        gay_msgs = [i.strip('\n') for i in f.read().split(';') if i.strip('\n')]
except FileNotFoundError:
    open('messages.txt', 'a').close()
    gay_msgs = None

if not gay_msgs:
    print('Почему messages.txt пустой? а? м? Что мне присылать?\n'
          'А ну бегом заполнять!')
    sys.exit()

vk_session = vk_api.VkApi(token=sys.argv[1])
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.from_chat:
        if event.user_id in id_of_gay:
            vk.messages.send(chat_id=event.chat_id,
                             message=random.choice(gay_msgs),
                             reply_to=event.message_id,
                             random_id=0)
