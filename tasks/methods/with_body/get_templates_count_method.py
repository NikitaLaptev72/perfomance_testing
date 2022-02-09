import common_functions.functions as fun
import random as rnd
import json


def get_templates_count(
        templates_Id,
        users_offices_ids,
        creators_ids,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(templates_Id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'getTemplatesCount',
                json.dumps(
                    {
                        "ids": [
                            i_number
                        ]
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'getTemplatesCount',
                json.dumps(
                    {
                        "ids": templates_Id[i:i+rnd.randint(1, 5)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(users_offices_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'getTemplatesCount',
                json.dumps(
                    {
                        "officesIds": [
                            i_number
                        ]
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'getTemplatesCount',
                json.dumps(
                    {
                        "officesIds": users_offices_ids[i:i+rnd.randint(1, 5)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(creators_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'getTemplatesCount',
                json.dumps(
                    {
                        "creators_ids": [
                            i_number
                        ]
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'getTemplatesCount',
                json.dumps(
                    {
                        "creators_ids": creators_ids[i:i+rnd.randint(1, 5)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
