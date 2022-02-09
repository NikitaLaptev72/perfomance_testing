import common_functions.functions as fun
import random as rnd
import json


def search_tasks_to_set_as_parent(
        tasks_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(tasks_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchTasksToSetAsParent',
                json.dumps(
                    {
                        "taskIds": [
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
                'searchTasksToSetAsParent',
                json.dumps(
                    {
                        "taskIds": [
                            i_number
                        ],
                        "searchParams": {
                            "limit": rnd.randint(3, 10)
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
                'searchTasksToSetAsParent',
                json.dumps(
                    {
                        "taskIds": tasks_id[i:i+rnd.randint(1, 5)]
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchTasksToSetAsParent',
                json.dumps(
                    {
                        "taskIds": tasks_id[i:i+rnd.randint(1, 5)],
                        "searchParams": {
                            "limit": rnd.randint(3, 10)
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*4

    return count_of_request, list_of_ammo
