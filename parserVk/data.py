from .captcha import auth_vk

# Список полей для того чтобы видеть нужную информацию
USER_FIELDS = "photo_max," "domain," "sex," "bdate," \
              "followers_count," "online," "last_seen,"  \
              "contacts," "status," "city," "country,"  \
              "site," "verified," "about,"

GROUP_FIELDS = 'verified,' 'members_count,' 'status,' 'description,' 'city,' 'country,' 'site,'

vk = auth_vk()


class Data:
    """
        Собираем данные пользователя и группы вконтакте.
        Данные собирается с помощью библиотекой vk_api.
        Познакомится с библиотекой можете здесь --> https://dev.vk.com/reference
    """
    def __init__(self):
        self._uncollected_data = []


class UserData(Data):
    """ Получаем данные пользователя методом users.get
        Подробнее о методе можете узнать по ссылке --> https://dev.vk.com/method/users.get
    """
    def get(self, user_ids):
        data = vk.users.get(user_ids=user_ids, fields=USER_FIELDS)
        for i in data:
            self._uncollected_data.append(i)
        return self._uncollected_data


class GroupData(Data):
    """ Получаем данные группы методом getById.get
        Подробнее о методе можете узнать по ссылке --> https://dev.vk.com/method/groups.getById
    """
    def get(self, group_ids):
        data = vk.groups.getById(group_ids=group_ids, fields=GROUP_FIELDS)
        for i in data:
            self._uncollected_data.append(i)
        return self._uncollected_data
