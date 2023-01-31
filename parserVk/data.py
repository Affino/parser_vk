from .captcha import auth_vk

USER_FIELDS = "photo_max," "domain," "sex," "bdate," \
              "followers_count," "online," "last_seen,"  \
              "contacts," "status,"

GROUP_FIELDS = 'members_count,' 'status,' 'description'

vk = auth_vk()


class Data:
    def __init__(self):
        self._uncollected_data = []


class UserData(Data):
    def get(self, user_ids):
        data = vk.users.get(user_ids=user_ids, fields=USER_FIELDS)
        for i in data:
            self._uncollected_data.append(i)
        return self._uncollected_data


class GroupData(Data):
    def get(self, group_ids):
        data = vk.groups.getById(group_ids=group_ids, fields=GROUP_FIELDS)
        for i in data:
            self._uncollected_data.append(i)
        return self._uncollected_data
