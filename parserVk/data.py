from captcha import

class Data:
    def __init__(self, fields, vk):
        self._fields = fields
        self._vk = vk


class UserData(Data):

    @staticmethod
    def get(self, user_ids):
        uncollected_data = []
        data = vk.users.get(user_ids=user_ids, fields=fields)
        for i in data:
            uncollected_data.append(i)


class GroupData(Data):
    pass