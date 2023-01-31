from datetime import datetime


class ExtractingData:
    def __init__(self):
        self.collected_data = {}


class ExtractingUserData(ExtractingData):
    def __init__(self):
        super().__init__()

    def extract_str_data(self, data: str, key):
        if 'domain' == key:
            domain = data
            self.collected_data['user_url'] = f'https://vk.com/{domain}'
        if 'first_name' == key or 'last_name' == key:
            self.collected_data[key] = data
        if 'photo_max' == key:
            self.collected_data['photo'] = data
        if 'bdate' == key:
            self.collected_data['bdate'] = data
        if 'status' == key:
            if bool(data) is True:
                self.collected_data['user_status'] = data
            else:
                self.collected_data['user_status'] = None

    def extract_int_data(self, data: int, key):
        if 'followers_count' == key:
            self.collected_data[key] = data
        if 'sex' == key:
            self.collected_data['gender'] = data
        if 'online' == key:
            self.collected_data['online_'] = data
        if 'mobile_phone' == key:
            self.collected_data['mobile_phone'] = data

    def extract_dict_data(self, data: dict, key):
        if 'last_seen' == key:
            time = data['time']
            dt_object = datetime.fromtimestamp(time)
            self.collected_data['last_seen'] = dt_object


class ExtractingGroupData(ExtractingData):
    def __init__(self):
        super().__init__()

    def extract_str_data(self, data: str, key):
        if 'screen_name' == key:
            self.collected_data['group_url'] = f'https://vk.com/{data}'
        if 'name' == key:
            self.collected_data['title'] = data
        if 'status' == key:
            self.collected_data['group_status'] = data
        if 'description' == key:
            self.collected_data[key] = data
        if 'type' == key:
            self.collected_data[key] = data

    def extract_int_data(self, data: int, key):
        if 'is_closed' == key:
            self.collected_data[key] = data
        if 'members_count' == key:
            self.collected_data[key] = data


def extract_user_data(uncollected_data):
    extracting = ExtractingUserData()

    for first_dict_key in uncollected_data.keys():
        data = uncollected_data[first_dict_key]
        if isinstance(data, str):
            extracting.extract_str_data(data, first_dict_key)

        if isinstance(data, int):
            extracting.extract_int_data(data, first_dict_key)

        if isinstance(data, dict):
            extracting.extract_dict_data(data, first_dict_key)

    return extracting.collected_data


def extract_group_data(uncollected_data):
    extracting = ExtractingGroupData()

    for first_dict_key in uncollected_data.keys():
        data = uncollected_data[first_dict_key]
        if isinstance(data, str):
            extracting.extract_str_data(data, first_dict_key)

        if isinstance(data, int):
            extracting.extract_int_data(data, first_dict_key)

        # if isinstance(data, dict):
        #     extracting.extract_dict_data(data, first_dict_key)

    return extracting.collected_data

