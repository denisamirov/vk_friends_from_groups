import requests
# Токен для твоего приложения. Получать тут: https://dev.vk.com/api/getting-started
token = '4ae054ce2581c3c3abe99cd5cd28v233ad359014ae054ce258cb5f024e744f7f34ac5159dcd442877c9a8c2948'
# Запрос на получение участников группы
u = 'https://api.vk.com/method/groups.getMembers?user_id=210700286&v=5.131'
# Параметры, которые надо передать с запросом
p = {'access_token': token, 'group_id': 151730617}
# Запрос на добавление в друзья
u_get_friend = 'https://api.vk.com/method/friends.add?user_id=210700286&v=5.131'
# Выполняем запрос на получение участников группы
a = requests.get(url=u, params=p)
x = 0
# В цикле проходимся по кажому участнику группы и шлем ему приглашение в друзья с сообщением
for i in a.json()['response']['items']:
    p_get_friend = {'access_token': token, 'text': 'Привет!\n'
                                                   'Интересует взаиманя подписка?!\n'
                                                   'Моя группа https://vk.com/club199796068\n'
                                                   'Подпишусь на тебя взаимно!😄',
                    'user_id': i}
    fr_get = requests.get(url=u_get_friend, params=p_get_friend)
    print(fr_get.json())
    x = x + 1

print('Количество отправленных заявок - ', x)
