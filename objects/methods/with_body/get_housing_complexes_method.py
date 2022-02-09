import common_functions.functions as fun
import random as rnd
import json


def get_housing_complexes(
        housing_complexes_id,
        developer_housing_complexes_id,
        adresses_id, count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'id',
        'name',
        'addressId',
        'createdAt',
        'deletedAt',
        'isActive',
        'officeId',
        'developer',
        'slogan',
        'description',
        'viewingTimeFromWeekdays',
        'viewingTimeToWeekdays',
        'viewingTimeFromWeekend',
        'viewingTimeToWeekend',
        'advantages',
        'promotions',
        'responsibles',
        'schema',
        'characteristic'
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for j, j_number in enumerate(fields):
        for i, i_number in enumerate(housing_complexes_id):
            if (len(housing_complexes_id) < 3):
                fun.add_to_list(
                    list_of_ammo,
                    fun.create_req_string_empty_params(
                        'objects',
                        'getHousingComplexes',
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
            else:
                fun.add_to_list(
                    list_of_ammo,
                    fun.create_req_string_empty_params(
                        'objects',
                        'getHousingComplexes',
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
                        'getHousingComplexes',
                        json.dumps(
                            {
                                "fields": [
                                    j_number
                                ],
                                "ids": housing_complexes_id[i:i+rnd.randint(1, 3)]
                            },
                            default=str
                        )
                    )
                )

    count_of_request += i*j*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for j, j_number in enumerate(fields):
        for i, i_number in enumerate(developer_housing_complexes_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'objects',
                    'getHousingComplexes',
                    json.dumps(
                        {
                            "fields": [
                                j_number
                            ],
                            "developerIds": [
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
                    'getHousingComplexes',
                    json.dumps(
                        {
                            "fields": [
                                j_number
                            ],
                            "developerIds": developer_housing_complexes_id[i:i+rnd.randint(1, 3)]
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*j*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for j, j_number in enumerate(fields):
        for i, i_number in enumerate(adresses_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'objects',
                    'getHousingComplexes',
                    json.dumps(
                        {
                            "fields": [
                                j_number
                            ],
                            "addressIds": [
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
                    'getHousingComplexes',
                    json.dumps(
                        {
                            "fields": [
                                j_number
                            ],
                            "addressIds": adresses_id[i:i+rnd.randint(1, 3)]
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*j*2

    return count_of_request, list_of_ammo
