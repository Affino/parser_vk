from itertools import zip_longest

from parserVk.data import *
from parserVk.extract import extract_user_data, extract_group_data
from parserVk.save import save
from mysql.execute import Query


query = Query('db')
data = Data()

# -----ID-----
user_ids = query.select_value('vk_info', 'user_id')
group_ids = query.select_value('vk_info', 'group_id')


# -----USER DATA-----
def parse_users():
    user_data = UserData()
    uncollected_data = user_data.get(user_ids)
    for i, user_id in zip_longest(uncollected_data, user_ids):
        if user_id is not None and i is not None:
            collected_data = extract_user_data(i)
            save('vk_info', collected_data, query, 'user_id', user_id)


# -----GROUP DATA-----
def parse_groups():
    group_data = GroupData()
    uncollected_data = group_data.get(group_ids)
    for i, group_id in zip_longest(uncollected_data, group_ids):
        if group_id and i is not None:
            collected_data = extract_group_data(i)
            save('vk_info', collected_data, query, 'group_id', group_id)


def main():
    parse_users()
    parse_groups()


if __name__ == '__main__':
    main()
