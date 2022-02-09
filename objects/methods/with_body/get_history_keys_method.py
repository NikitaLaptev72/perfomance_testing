import common_functions.functions as fun
import random as rnd
import json


def get_history_keys(
        history_keys_id,
        object_ids,
        keys_id_history_keys_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(history_keys_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getHistoryKeys',
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
                'getHistoryKeys',
                json.dumps(
                    {
                        "ids": history_keys_id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(object_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getHistoryKeys',
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
                'getHistoryKeys',
                json.dumps(
                    {
                        "objectIds": object_ids[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(keys_id_history_keys_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getHistoryKeys',
                json.dumps(
                    {
                        "keyIds": [
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
                'getHistoryKeys',
                json.dumps(
                    {
                        "keyIds": keys_id_history_keys_id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
