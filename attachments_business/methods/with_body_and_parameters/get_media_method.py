import common_functions.functions as fun
import json
import random as rnd


def get_media(
        attachments_id,
        entity_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    category_id = [i for i in range(1, 5)]
    entity = [i for i in range(1, 92)]

    for i, i_number in enumerate(category_id):
        for j, j_number in enumerate(attachments_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'attachments-business',
                    'getMedia',
                    json.dumps(
                        {
                            "categoryId": i_number
                        },
                        default=str
                    ),
                    json.dumps(
                        {
                            "ids": [
                                j_number
                            ]
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*j

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(category_id):
        for j, j_number in enumerate(attachments_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'attachments-business',
                    'getMedia',
                    json.dumps(
                        {
                            "categoryId": i_number
                        },
                        default=str
                    ),
                    json.dumps(
                        {
                            "ids": attachments_id[j:j+rnd.randint(1, 5)]
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*j

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(category_id):
        for k, k_number in enumerate(entity):
            for j, j_number in enumerate(entity_id):
                fun.add_to_list(
                    list_of_ammo,
                    fun.create_req_string_with_parameters_body(
                        'attachments-business',
                        'getMedia',
                        json.dumps(
                            {
                                "categoryId": i_number
                            },
                            default=str
                        ),
                        json.dumps(
                            {
                                "relations": [
                                    {
                                        "entity": k_number,
                                        "entityId": j_number
                                    }
                                ]
                            },
                            default=str
                        )
                    )
                )

    count_of_request += i*j*k

    return count_of_request, list_of_ammo
