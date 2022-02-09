import common_functions.functions as fun
import random as rnd
import json


def get_members(
        members_ids,
        tasks_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(members_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'getMembers',
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
                'getMembers',
                json.dumps(
                    {
                        "ids": tasks_id[i:i+rnd.randint(1, 5)]
                    },
                    default=str
                )
            )
        )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(tasks_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'tasks',
                    'getMembers',
                    json.dumps(
                        {
                            "taskId": [
                                i_number
                            ]
                        },
                        default=str
                    )
                )
            )
        count_of_request += i

    return count_of_request, list_of_ammo
