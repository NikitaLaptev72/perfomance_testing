import common_functions.functions as fun
import random as rnd
import json


def get_count_tasks(
        tasks_id,
        created_at_task,
        description_task,
        count_of_request,
        duration,
        list_of_ammo
        ):
    for i, i_number in enumerate(tasks_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'getCountTasks',
                json.dumps(
                    {
                        "operands": {
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
                'getCountTasks',
                json.dumps(
                    {
                        "operands": {
                            "ids": tasks_id[i:i+rnd.randint(1, 5)]
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(created_at_task):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'getCountTasks',
                json.dumps(
                    {
                        "operands": {
                            "createdAt": [
                                i_number
                            ]
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(description_task):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'getCountTasks',
                json.dumps(
                    {
                        "operands": {
                            "description": i_number
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    return count_of_request, list_of_ammo
