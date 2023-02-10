import pymysql


class Query:
    def __init__(self, db=None):
        self._connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            db=db
        )
        self._cursor = self._connection.cursor()
        print(f"Connected database: {db}")

    def select_value(self, table, column):
        values = []
        self._cursor.execute("SELECT %s FROM %s ORDER BY id" % (column, table))

        values_in_tuple = self._cursor.fetchall()
        for value_in_tuple in values_in_tuple:
            value = value_in_tuple[0]
            values.append(value)
        return values

    def update(self, table, column1, column2, vk_id):
        """ Обновить старое значение """
        query_update = f"UPDATE {table} SET {column1} WHERE {column2} = {vk_id}"
        self._cursor.execute(query_update)
        self._connection.commit()
