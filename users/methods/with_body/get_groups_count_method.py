import common_functions.functions as fun
import json


def get_groups_count(
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
                    'getGroupsCount',
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

    count_of_request += i*j

    return count_of_request, list_of_ammo
