import common_functions.functions as fun
import json


def get_template(
        templates_Id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    appends = [
        'checklist',
        'members',
        'offices',
        'fields'
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for append in appends:
        for i, i_number in enumerate(templates_Id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_body(
                    'tasks',
                    'getTemplate',
                    json.dumps(
                        {
                            "templateId": i_number,
                            "appends": append
                        },
                        default=str
                    )
                )
            )
    count_of_request += i*len(appends)

    return count_of_request, list_of_ammo
