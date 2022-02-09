import common_functions.functions as fun
import random as rnd
import json


def get_upper_hierarchy(
        users_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'id',
        'firstName',
        'lastName',
        'middleName',
        'fullName',
        'positionId',
        'options'
    ]
    generated_fields = fun.combinations(fields)
    generated_fields.pop(0)

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(users_id):
        for fields_kit in generated_fields:
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'users',
                    'getUpperHierarchy',
                    json.dumps(
                        {
                            "requestedUserId": i_number,
                            "fields": [
                                rnd.choice(fields_kit)
                            ]
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*len(generated_fields)

    return count_of_request, list_of_ammo
