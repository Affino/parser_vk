from itertools import zip_longest
import time

from parserVk.data import *
from parserVk.extract import filter_user_data, filter_group_data
from parserVk.save import save
from mysql.execute import Query


query = Query('db')
data = Data()


# -----USER DATA-----
def parse_users(ids):
    """ Парсить пользователя вконтакте с помощью vk id"""
    user_data = UserData()
    unfiltered_data = user_data.get(ids)
    for unf_data, vk_id in zip_longest(unfiltered_data, ids):
        filtered_data = filter_user_data(unf_data)
        save('vk_info', filtered_data, query, 'vk_id', vk_id)


# -----GROUP DATA-----
def parse_groups(ids):
    """ Парсить группы вконтакте с помощью vk id"""
    group_data = GroupData()
    unfiltered_data = group_data.get(ids)
    for unf_data, vk_id in zip_longest(unfiltered_data, ids):
        filtered_data = filter_group_data(unf_data)
        save('vk_info', filtered_data, query, 'vk_id', f'-{vk_id}')


def main():
    ids = query.select_value('vk_info', 'vk_id')  # получаем идентификаторы пользователя и группы
    # --- VK ID USERS
    user_ids = [i for i in ids if i is not None and '-' not in str(i)]
    # --- VK ID GROUPS ---
    group_ids_with_minus = [i for i in ids if i is not None and '-' in str(i)] # идентификаторы группы с знаком минусум
    group_ids = []  # идентификаторы группы без знака минуса
    for i in group_ids_with_minus:
        group_id = str(i).replace('-', '')
        group_ids.append(int(group_id))

    parse_users(user_ids)
    parse_groups(group_ids)


if __name__ == '__main__':
    while True:
        main()
