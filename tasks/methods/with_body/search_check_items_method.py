import common_functions.functions as fun
import random as rnd
import json


def search_check_items(
        checklists_id,
        tasks_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(checklists_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchCheckItems',
                json.dumps(
                    {
                        "searchFields": {
                            "ids": [
                                i_number
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
                'tasks',
                'searchCheckItems',
                json.dumps(
                    {
                        "searchFields": {
                            "ids": checklists_id[i:i+rnd.randint(1, 5)]
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for j, j_number in enumerate(tasks_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchCheckItems',
                json.dumps(
                    {
                        "searchFields": {
                            "taskId": j_number
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    return count_of_request, list_of_ammo
