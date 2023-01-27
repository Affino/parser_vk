from mysql.execute import Query

query = Query('db')
user_ids = query.select_value('vk_info', 'user_id')
for id in user_ids:
    query.update('vk_info', 'first_name="Anonym"', 'user_id', id)