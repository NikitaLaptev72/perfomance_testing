import common_functions.functions as fun
import json


def get_task(
        tasks_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    appends = [
        'entities',
        'members',
        'substatus',
        'completion'
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for append in appends:
        for i, i_number in enumerate(tasks_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_body(
                    'tasks',
                    'getTask',
                    json.dumps(
                        {
                            "taskId": i_number,
                            "appends": append
                        },
                        default=str
                    )
                )
            )
    count_of_request += i*len(appends)

    return count_of_request, list_of_ammo
