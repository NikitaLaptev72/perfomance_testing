import common_functions.functions as fun
import random as rnd
import json


def get_streets(
        cities_id,
        districts_id,
        streets_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(cities_id):
        for j, j_number in enumerate(streets_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getStreets',
                    json.dumps(
                        {
                            "cities": i_number,
                            "ids": j_number
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getStreets',
                    json.dumps(
                        {
                            "cities": cities_id[i:i+rnd.randint(1, 5)],
                            "ids": streets_id[j:j+rnd.randint(1, 5)]
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*j

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for j, j_number in enumerate(districts_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'getStreets',
                json.dumps(
                    {
                        "cities": i_number,
                        "districts": j_number
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'getStreets',
                json.dumps(
                    {
                        "cities": cities_id[i:i+rnd.randint(1, 5)],
                        "districts": districts_id[j:j+rnd.randint(1, 5)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*j

    return count_of_request, list_of_ammo
