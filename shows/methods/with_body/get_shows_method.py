import common_functions.functions as fun
import random as rnd
import json


def get_shows(
        tickets_id,
        shows_id,
        status_shows_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'id',
        'status',
        'showDate',
        'createdAt',
        'data',
        'note'
    ]

    for i, i_number in enumerate(tickets_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'shows',
                'getShows',
                json.dumps(
                    {
                        "ticketIds": [
                            i_number
                        ],
                        "fields": [
                            rnd.choice(fields)
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
                'getShows',
                json.dumps(
                    {
                        "ticketIds": tickets_id[i:i+rnd.randint(1, 5)],
                        "fields": [
                            rnd.choice(fields)
                        ]
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
                'getShows',
                json.dumps(
                    {
                        "ids": [
                            i_number
                        ],
                        "fields": [
                            rnd.choice(fields)
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
                'getShows',
                json.dumps(
                    {
                        "ids": shows_id[i:i+rnd.randint(1, 5)],
                        "fields": [
                            rnd.choice(fields)
                        ]
                    },
                    default=str
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
                'getShows',
                json.dumps(
                    {
                        "statuses": [
                            i_number
                        ],
                        "fields": [
                            rnd.choice(fields)
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
                'getShows',
                json.dumps(
                    {
                        "statuses": status_shows_id[i:i+rnd.randint(1, 5)],
                        "fields": [
                            rnd.choice(fields)
                        ]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
