import common_functions.functions as fun
import random as rnd
import json


def count_in_phone_book(
        realtors_id,
        cities_id,
        agencies_id,
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
                'countInPhoneBook',
                json.dumps(
                    {
                        "params": {
                            "ids": [
                                    i_number
                            ]
                        }
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'clients',
                'countInPhoneBook',
                json.dumps(
                    {
                        "params": {
                            "ids": realtors_id[i:i+rnd.randint(1, 3)]
                        }
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
                'countInPhoneBook',
                json.dumps(
                    {
                        "params": {
                            "cityIds": [
                                i_number
                            ]
                        }
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo, fun.create_req_string_empty_params(
                'clients',
                'countInPhoneBook',
                json.dumps(
                    {
                        "params": {
                            "cityIds": realtors_id[i:i+rnd.randint(1, 3)]
                        }
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
                'countInPhoneBook',
                json.dumps(
                    {
                        "params": {
                            "agencyIds": [
                                i_number
                            ]
                        }
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'clients',
                'countInPhoneBook',
                json.dumps(
                    {
                        "params": {
                            "agencyIds": realtors_id[i:i+rnd.randint(1, 3)]
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
