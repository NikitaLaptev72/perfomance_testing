import common_functions.functions as fun
import random as rnd
import json


def search_groups(
        users_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    op = [
        '=',
        '!=',
        '<>',
        '>',
        '>=',
        '<',
        '<='
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for j, j_number in enumerate(op):
        for i, i_number in enumerate(users_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'users',
                    'searchGroups',
                    json.dumps(
                        {
                            "filter": [
                                {
                                    "field": "id",
                                    "op": j_number,
                                    "value": i_number
                                }
                            ]
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'users',
                    'searchGroups',
                    json.dumps(
                        {
                            "filter": [
                                {
                                    "field": "id",
                                    "op": j_number,
                                    "value": i_number
                                }
                            ],
                            "options": {
                                "limit": rnd.randint(3, 10)
                            }
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*j*2

    return count_of_request, list_of_ammo
