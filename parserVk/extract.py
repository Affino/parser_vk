class DataFiltering:
    """ Фильтрация данных """
    def __init__(self):
        self.filtered_data = {}


class UserDataFiltering(DataFiltering):
    def __init__(self):
        super().__init__()

    def filter_str_data(self, data: str, key):
        if 'first_name' == key:
            self.filtered_data['name'] = data
            self.filtered_data['is_group'] = 0
        elif 'last_name' == key:
            self.filtered_data['name'] += f' {data}'
        if 'photo_max' == key:
            self.filtered_data['photo'] = data
        if 'about' == key:
            self.filtered_data['description'] = data
        if 'site' == key:
            self.filtered_data['site'] = data
        if 'mobile_phone' == key:
            self.filtered_data['contact'] = data
        if 'status' == key:
            if bool(data) is True:
                self.filtered_data['status'] = data
            else:
                self.filtered_data['status'] = None

    def filter_int_data(self, data: int, key):
        if 'id' == key:
            self.filtered_data['url'] = f'https://vk.com/id{data}'
        if 'is_closed' == key:
            if data is False:
                self.filtered_data[key] = 0
            else:
                self.filtered_data[key] = 1
        if 'followers_count' == key:
            self.filtered_data[key] = data
        if 'verified' == key:
            self.filtered_data['verified'] = data

    def filter_dict_data(self, data: dict, key):
        if 'city' == key:
            city = data['title']
            self.filtered_data['city'] = city
        if 'country' == key:
            country = data['title']
            self.filtered_data['country'] = country


class GroupDataFiltering(DataFiltering):
    def __init__(self):
        super().__init__()

    def filter_str_data(self, data: str, key):
        if 'name' == key:
            self.filtered_data['name'] = data
            self.filtered_data['is_group'] = 1
        if 'status' == key:
            self.filtered_data['status'] = data
        if 'photo_50' == key:
            self.filtered_data['photo'] = data
        if 'description' == key:
            self.filtered_data[key] = data
        if 'site' == key:
            self.filtered_data['site'] = data

    def filter_dict_data(self, data: dict, key):
        if 'city' == key:
            city = data['title']
            self.filtered_data['city'] = city
        if 'country' == key:
            country = data['title']
            self.filtered_data['country'] = country

    def filter_int_data(self, data: int, key):
        if 'id' == key:
            self.filtered_data['url'] = f'https://vk.com/public{data}'
        if 'is_closed' == key:
            self.filtered_data[key] = data
        if 'members_count' == key:
            self.filtered_data['followers_count'] = data
        if 'verified' == key:
            self.filtered_data['verified'] = data


def filter_user_data(uncollected_data):
    extracting = UserDataFiltering()

    for first_dict_key in uncollected_data.keys():
        data = uncollected_data[first_dict_key]
        if isinstance(data, str):
            extracting.filter_str_data(data, first_dict_key)
        if isinstance(data, int):
            extracting.filter_int_data(data, first_dict_key)
        if isinstance(data, dict):
            extracting.filter_dict_data(data, first_dict_key)

    return extracting.filtered_data


def filter_group_data(unfiltered_data):
    extracting = GroupDataFiltering()

    for first_dict_key in unfiltered_data.keys():
        data = unfiltered_data[first_dict_key]
        if isinstance(data, str):
            extracting.filter_str_data(data, first_dict_key)
        if isinstance(data, int):
            extracting.filter_int_data(data, first_dict_key)
        if isinstance(data, dict):
            extracting.filter_dict_data(data, first_dict_key)

    return extracting.filtered_data
