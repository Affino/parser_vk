from parserVk.data import *
from parserVk.extract import *
from mysql.execute import Query

query = Query('db')
data = Data()

# -----ID-----
user_ids = query.select_value('vk_info', 'user_id')
group_ids = query.select_value('vk_info', 'group_id')

# -----USER DATA-----
user_data = UserData()
uncollected_data = user_data.get(user_ids)
for i in uncollected_data:
    collected_data = extract_user_data(i)


# -----GROUP DATA-----
group_data = GroupData()
uncollected_data = group_data.get(group_ids)
for i in uncollected_data:
    collected_data = extract_group_data(i)




