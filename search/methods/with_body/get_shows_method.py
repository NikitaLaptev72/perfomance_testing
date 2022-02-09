import common_functions.functions as fun
import random as rnd
import json


def get_shows(
        users_id,
        realtors_id,
        contacts_id,
        addresses_id,
        shows_id,
        tickets_id,
        object_ids,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(users_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getShows',
                json.dumps(
                    {
                        "userId": i_number
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(realtors_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getShows',
                json.dumps(
                    {
                        "realtorId": i_number
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(contacts_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getShows',
                json.dumps(
                    {
                        "clientId": i_number
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(addresses_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getShows',
                json.dumps(
                    {
                        "addressId": i_number
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(shows_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getShows',
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
                'search',
                'getShows',
                json.dumps(
                    {
                        "ids": shows_id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(tickets_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getShows',
                json.dumps(
                    {
                        "ticketIds": [
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
                'search',
                'getShows',
                json.dumps(
                    {
                        "ticketIds": tickets_id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(object_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getShows',
                json.dumps(
                    {
                        "objectIds": [
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
                'search',
                'getShows',
                json.dumps(
                    {
                        "objectIds": object_ids[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
