import common_functions.functions as fun
import random as rnd
import json


def get_realtors_count(
        realtors_id,
        cities_id,
        agencies_id,
        realtors_full_name,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(realtors_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'clients',
                'getRealtorsCount',
                json.dumps(
                    {
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
                'clients',
                'getRealtorsCount',
                json.dumps(
                    {
                        "ids": realtors_id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(cities_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'clients',
                'getRealtorsCount',
                json.dumps(
                    {
                        "cityIds": [
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
                'clients',
                'getRealtorsCount',
                json.dumps(
                    {
                        "cityIds": [
                            cities_id[i:i+rnd.randint(1, 3)]
                        ]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(agencies_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'clients',
                'getRealtorsCount',
                json.dumps(
                    {
                        "agencyIds": [
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
                'clients',
                'getRealtorsCount',
                json.dumps(
                    {
                        "agencyIds": agencies_id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(realtors_full_name):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'clients',
                'getRealtorsCount',
                json.dumps(
                    {
                        "fullName": i_number
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    return count_of_request, list_of_ammo
