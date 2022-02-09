import common_functions.functions as fun
import random as rnd
import json


def get_count_shows(
        tickets_id,
        shows_id,
        status_shows_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(tickets_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'shows',
                'getCountShows',
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
                'shows',
                'getCountShows',
                json.dumps(
                    {
                        "ticketIds": tickets_id[i:i+rnd.randint(1, 5)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(shows_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'shows',
                'getCountShows',
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
                'shows',
                'getCountShows',
                json.dumps(
                    {
                        "ids": shows_id[i:i+rnd.randint(1, 5)]
                    }
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(status_shows_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'shows',
                'getCountShows',
                json.dumps(
                    {
                        "statuses": [
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
                'shows',
                'getCountShows',
                json.dumps(
                    {
                        "statuses": status_shows_id[i:i+rnd.randint(1, 5)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
