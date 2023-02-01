from itertools import zip_longest
import time

from parserVk.data import *
from parserVk.extract import extract_user_data, extract_group_data
from parserVk.save import save
from mysql.execute import Query


query = Query('db')
data = Data()


# -----USER DATA-----
def parse_users(ids):
    user_data = UserData()
    uncollected_data = user_data.get(ids)
    for i, user_id in zip_longest(uncollected_data, ids):
        collected_data = extract_user_data(i)
        save('vk_info', collected_data, query, 'user_id', user_id)


# -----GROUP DATA-----
def parse_groups(ids):
    group_data = GroupData()
    uncollected_data = group_data.get(ids)
    for i, group_id in zip_longest(uncollected_data, ids):
        collected_data = extract_group_data(i)
        save('vk_info', collected_data, query, 'group_id', group_id)


def main():
    # -----ID-----
    ids = query.select_value('vk_info', 'user_id')
    user_ids = [i for i in ids if i is not None]
    ids = query.select_value('vk_info', 'group_id')
    group_ids = [i for i in ids if i is not None]

    parse_users(user_ids)
    parse_groups(group_ids)


if __name__ == '__main__':
    while True:
        main()
