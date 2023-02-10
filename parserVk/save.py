def save(table: str, data, query, column_id, vk_id):
    """ Сохранить данные в база данных """

    column = ''
    for key, value in data.items():
        column += f' {key}="{value}",'
    column = column.replace('"None"', 'Null')
    column = column.strip(',')
    query.update(table, column, column_id, vk_id)
