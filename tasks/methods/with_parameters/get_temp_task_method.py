import common_functions.functions as fun
import json


def get_temp_task(
        temp_tasks_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    appends = [
        'checklist',
        'members',
        'entities',
        'taskParent',
        'fieldValues',
        'substatusId'
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for append in appends:
        for i, i_number in enumerate(temp_tasks_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_body(
                    'tasks',
                    'getTempTask',
                    json.dumps(
                        {
                            "tempTaskId": i_number,
                            "appends": append
                        },
                        default=str
                    )
                )
            )
    count_of_request += i*len(appends)

    return count_of_request, list_of_ammo
