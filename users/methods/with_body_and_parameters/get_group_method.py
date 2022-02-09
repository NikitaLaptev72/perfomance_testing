import common_functions.functions as fun
import json


def get_group(
        groups_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'id',
        'title',
        'description',
        'creatorId'
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    generated_fields = fun.combinations(fields)
    generated_fields.pop(0)

    for i, i_number in enumerate(groups_id):
        for fields_kit in generated_fields:
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'users',
                    'getGroup',
                    json.dumps(
                        {
                            "groupId": i_number
                        },
                        default=str
                    ),
                    json.dumps(
                        [
                            ", ".join(fields_kit)
                        ],
                        default=str
                    )
                )
            )

    count_of_request += i*len(generated_fields)

    return count_of_request, list_of_ammo
