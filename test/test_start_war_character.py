import pytest
import json
import utils

ddt = utils.DDT()


@pytest.fixture(scope='session')
def get_all_people():
    input_data = ddt.validate_number_of_characters()
    url = input_data[0][0]
    response_list = []
    is_next_available = True
    while is_next_available:
        response = utils.get_response(url, input_data[2][0])
        response_data = response.json()
        for result in response_data['results']:
            response_list.append(result)
        if response_data['next'] is not None:
            url = response_data['next']
        else:
            is_next_available = False
    return response_list


@pytest.mark.parametrize("expected_result", ddt.validate_number_of_characters()[1])
def test_validate_number_of_characters(get_all_people, expected_result):
    assert len(get_all_people) == int(expected_result)


@pytest.mark.parametrize("expected_result", ddt.validate_character_is_available_in_api())
def test_validate_character_is_available_in_api(get_all_people, expected_result):
    names_list = []
    for names in get_all_people:
        names_list.append(names['name'])
    assert expected_result in names_list


@pytest.mark.parametrize("url,expected_result_field, expected_result,payload", ddt.validate_details_of_a_specific_character())
def test_validate_details_of_a_specific_character(url,expected_result_field, expected_result,payload):
    response = utils.get_response(url, payload)
    actual_response= response.json()
    expected_result_field_list = utils.convert_string_to_list(expected_result_field, ",")
    expected_response = utils.convert_list_to_dict(expected_result_field_list,
                                                   utils.convert_string_to_list(expected_result, ","))
    for value in expected_result_field_list:
        assert actual_response[value] == expected_response[value]


@pytest.mark.parametrize("url, expected_result,payload", ddt.validate_response_code())
def test_validate_response_code(url,expected_result,payload):
    response = utils.get_response(url, payload)
    assert response.status_code == int(expected_result)


@pytest.mark.parametrize("url,expected_result_field, expected_result,payload", ddt.validate_type_of_field_in_response())
def test_validate_type_of_field_in_response(url,expected_result_field, expected_result,payload):
    response = utils.get_response(url, payload)
    actual_response= response.json()
    expected_result_field_list = utils.convert_string_to_list(expected_result_field, ",")
    expected_response = utils.convert_list_to_dict(expected_result_field_list,
                                                   utils.convert_string_to_list(expected_result, ","))
    for value in expected_result_field_list:

        assert isinstance(actual_response[value], eval(expected_response[value]))
