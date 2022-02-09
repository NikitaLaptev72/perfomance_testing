import common_functions.functions as fun
import random as rnd
import json


def search_user_settings(
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
            if (j != 0):
                fun.add_to_list(
                    list_of_ammo,
                    fun.create_req_string_empty_params(
                        'users',
                        'searchUserSettings',
                        json.dumps(
                            {
                                "filter": [
                                    {
                                        "field": "userId",
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
            else:
                fun.add_to_list(
                    list_of_ammo,
                    fun.create_req_string_empty_params(
                        'users',
                        'searchUserSettings',
                        json.dumps(
                            {
                                "filter": [
                                    {
                                        "field": "userId",
                                        "op": j_number,
                                        "value": i_number
                                    }
                                ]
                            },
                            default=str
                        )
                    )
                )

    count_of_request += i*j

    return count_of_request, list_of_ammo
