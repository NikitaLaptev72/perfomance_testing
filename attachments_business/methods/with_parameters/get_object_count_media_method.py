import common_functions.functions as fun
import json


def get_object_count_media(
        entity_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    entity = [i for i in range(1, 92)]

    for i, i_number in enumerate(entity):
        for j, j_number in enumerate(entity_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_body(
                    'attachments-business',
                    'getObjectCountMedia',
                    json.dumps(
                        {
                            "entity": i_number,
                            "entityId": j_number
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*j

    return count_of_request, list_of_ammo
