import common_functions.functions as fun
import random as rnd
import json


def get_keys(
        keys_Id,
        object_ids,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(keys_Id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getKeys',
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
                'objects',
                'getKeys',
                json.dumps(
                    {
                        "ids": keys_Id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(object_ids):
        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getKeys',
                json.dumps(
                    {
                        "objectIds": [
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
                'objects',
                'getKeys',
                json.dumps(
                    {
                        "objectIds": object_ids[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
