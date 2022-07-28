import pandas
import requests


def get_response(url, header):
    return requests.get(url, header)


def convert_list_to_dict(key,items):
    return {key[i]: items[i] for i in range(len(key))}


def convert_string_to_list(str, delimiter):
    return list(str.split(delimiter))


class DDT:

    def __init__(self):
        test_data_df = pandas.read_csv("./resources/dtt_search_characters.csv")
        grouped_frame = test_data_df.groupby('Test case')
        self.grouped_data_frame = grouped_frame

    def validate_number_of_characters(self):
        for name, group in self.grouped_data_frame:
            if "validate number of characters".upper() in name.upper():
                return group['URL'].tolist(), group['Expected Result'].tolist(), group['payload'].tolist()

    def validate_character_is_available_in_api(self):
        for name, group in self.grouped_data_frame:
            if "Validate character is available in API".upper() in name.upper():
                return group['Expected Result'].tolist()

    def validate_details_of_a_specific_character(self):
        for name, group in self.grouped_data_frame:
            if "Validate details of a specific character".upper() in name.upper():
                return list (zip(group['URL'], group['Expected Result Field'], group[
                    'Expected Result'], group['payload']))

    def validate_response_code(self):
        for name, group in self.grouped_data_frame:
            if "Validate response code".upper() in name.upper():
                return list (zip(group['URL'], group[
                    'Expected Result'], group['payload']))

    def validate_type_of_field_in_response(self):
        for name, group in self.grouped_data_frame:
            if "Validate type of the field in the response".upper() in name.upper():
                return list (zip(group['URL'], group['Expected Result Field'], group[
                    'Expected Result'], group['payload']))
