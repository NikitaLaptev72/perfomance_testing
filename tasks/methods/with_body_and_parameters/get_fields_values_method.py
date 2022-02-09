import common_functions.functions as fun
import random as rnd
import json


def get_fields_values(
        tasks_id,
        field_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(tasks_id):
        for j, j_number in enumerate(field_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'tasks',
                    'getFieldsValues',
                    json.dumps(
                        {
                            "taskId": i_number
                        },
                        default=str
                    ),
                    json.dumps(
                        [
                            j_number
                        ],
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'tasks',
                    'getFieldsValues',
                    json.dumps(
                        {
                            "taskId": i_number
                        },
                        default=str
                    ),
                    json.dumps(
                        field_id[j:j+rnd.randint(1, 5)],
                        default=str
                    )
                )
            )

    count_of_request += i*j

    return count_of_request, list_of_ammo
