import common_functions.functions as fun
import random as rnd
import json


def get_districts(
        cities_id,
        districts_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(cities_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'getDistricts',
                json.dumps(
                    {
                        "cityIds": i_number
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'getDistricts',
                json.dumps(
                    {
                        "cityIds": cities_id[i:i+rnd.randint(1, 5)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(districts_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'getDistricts',
                json.dumps(
                    {
                        "ids": i_number
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'getDistricts',
                json.dumps(
                    {
                        "ids": districts_id[i:i+rnd.randint(1, 5)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
