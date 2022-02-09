import common_functions.functions as fun
import random as rnd
import json


def get_office_users(
        offices_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        '"*"',
        '"lastName"',
        '"firstName"',
        '"middleName"',
        '"lastName", "firstName"',
        '"lastName", "middleName"',
        '"firstName", "middleName"',
        '"lastName", "firstName", "middleName"'
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for combination in fields:
        for i, i_number in enumerate(offices_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'users',
                    'getOfficeUsers',
                    json.dumps(
                        {
                            "officesIds": i_number,
                            "options": {
                                "fields": [
                                    str(combination).replace("'", '')
                                ]
                            }
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'users',
                    'getOfficeUsers',
                    json.dumps(
                        {
                            "officesIds": i_number,
                            "options": {
                                "fields": [
                                    str(combination).replace("'", '')
                                ],
                                "limit": rnd.randint(3, 10)
                            }
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*len(fields)

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for combination in fields:
        for i, i_number in enumerate(offices_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'users',
                    'getOfficeUsers',
                    json.dumps(
                        {
                            "officesIds": offices_id[i:i+rnd.randint(1, 3)],
                            "options": {
                                "fields": [
                                    str(combination).replace("'", '')
                                ]
                            }
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'users',
                    'getOfficeUsers',
                    json.dumps(
                        {
                            "officesIds": offices_id[i:i+rnd.randint(1, 3)],
                            "options": {
                                "fields": [
                                    str(combination).replace("'", '')
                                ],
                                "limit": rnd.randint(3, 10)
                            }
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*len(fields)

    return count_of_request, list_of_ammo
