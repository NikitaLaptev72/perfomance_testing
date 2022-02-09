import common_functions.functions as fun
import random as rnd
import json


def get_entrances(
        entrances_id,
        general_plan_entrances_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(entrances_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getEntrances',
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
                'getEntrances',
                json.dumps(
                    {
                        "ids": entrances_id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(general_plan_entrances_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getEntrances',
                json.dumps(
                    {
                        "generalPlanIds": [
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
                'getEntrances',
                json.dumps(
                    {
                        "generalPlanIds": general_plan_entrances_id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
