import common_functions.functions as fun
import json


def get_object_fields_values(
        object_ids,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(object_ids):

        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_with_parameters_body(
                'objects',
                'getObjectFieldsValues',
                json.dumps(
                    {
                        "objectId": [
                            i_number
                        ]
                    },
                    default=str
                ),
                json.dumps(
                    []
                )
            )
        )

    count_of_request += i

    return count_of_request, list_of_ammo
