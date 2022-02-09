import common_functions.functions as fun
import random as rnd
import json


def search_tasks(
        task_titles,
        tasks_id,
        description_task,
        users_offices_ids,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'id',
        'title',
        'categoryId',
        'startAt',
        'overAt',
        'description',
        'priorityId',
        'statusId',
        'availableToAll',
        'closeRole',
        'createdAt',
        'endedAt',
        'riesObjectId',
        'riesTicketId',
        'riesClientId',
        'youtrackLink',
        'officeId'
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(task_titles):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchTasks',
                json.dumps(
                    {
                        "searchFields": [
                            {
                                "operands":
                                {
                                    "title": i_number
                                }
                            }
                        ],
                        "fields": [
                            rnd.choice(fields)
                        ]
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(tasks_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchTasks',
                json.dumps(
                    {
                        "searchFields": [
                            {
                                "operands":
                                {
                                    "ids": [
                                        i_number
                                    ]
                                }
                            }
                        ],
                        "fields": [
                            rnd.choice(fields)
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
                'searchTasks',
                json.dumps(
                    {
                        "searchFields": [
                            {
                                "operands":
                                {
                                    "ids": tasks_id[i:i+rnd.randint(1, 5)]
                                }
                            }
                        ],
                        "fields": [
                            rnd.choice(fields)
                        ]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(description_task):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchTasks',
                json.dumps(
                    {
                        "searchFields": [
                            {
                                "operands":
                                {
                                    "description": i_number
                                }
                            }
                        ],
                        "fields": [
                            rnd.choice(fields)
                        ]
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(users_offices_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchTasks',
                json.dumps(
                    {
                        "searchFields": [
                            {
                                "operands":
                                {
                                    "officesIds": [
                                        i_number
                                    ]
                                }
                            }
                        ],
                        fields: [
                            rnd.choice(fields)
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
                'searchTasks',
                json.dumps(
                    {
                        "searchFields": [
                            {
                                "operands":
                                {
                                    "officesIds": users_offices_ids[i:i+rnd.randint(1, 5)]
                                }
                            }
                        ],
                        fields: [
                            rnd.choice(fields)
                        ]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
