def save(table, data, query, column_id, vk_id):
    """ Сохранить данные """

    column = ''
    for key, value in data.items():
        column += f' {key}="{value}",'
    column = column.replace('"None"', 'Null')
    column = column.strip(',')
    query.update(table, column, column_id, vk_id)
