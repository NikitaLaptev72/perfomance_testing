import common_functions.functions as fun
import random as rnd
import json


def get_promotions(
        promotions_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'id',
        'entityType',
        'entityId',
        'title',
        'description',
        'endDate'
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for j, j_number in enumerate(fields):
        for i, i_number in enumerate(promotions_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'objects',
                    'getPromotions',
                    json.dumps(
                        {
                            "fields": [
                                j_number
                            ],
                            "ids": [
                                i_number
                            ]
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'objects',
                    'getPromotions',
                    json.dumps(
                        {
                            "fields": [
                                j_number
                            ],
                            "ids": [
                                promotions_id[i:i+rnd.randint(1, 3)]
                            ]
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*2

    return count_of_request, list_of_ammo
