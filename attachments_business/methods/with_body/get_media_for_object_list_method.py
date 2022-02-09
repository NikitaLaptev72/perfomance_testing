import common_functions.functions as fun
import json
import random as rnd


def get_media_for_object_list(
        entity_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    entity_type = [
        3,
        22
    ]

    for i, i_number in enumerate(entity_type):
        for j, j_number in enumerate(entity_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'attachments-business',
                    'getMediaForObjectList',
                    json.dumps(
                        {
                            "entityIds": [
                                j_number
                            ],
                            "entityType": i_number
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*j

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(entity_type):
        for j, j_number in enumerate(entity_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'attachments-business',
                    'getMediaForObjectList',
                    json.dumps(
                        {
                            "entityIds": entity_id[j:j+rnd.randint(1, 5)],
                            "entityType": i_number
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*j

    return count_of_request, list_of_ammo
