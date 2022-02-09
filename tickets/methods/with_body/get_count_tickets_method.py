import common_functions.functions as fun
import random as rnd
import json


def get_count_tickets(
        clients_id,
        tickets_id,
        offices_ids,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(clients_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tickets',
                'getCountTickets',
                json.dumps(
                    {
                        "clientIds": [
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
                'tickets',
                'getCountTickets',
                json.dumps(
                    {
                        "clientIds": clients_id[i:i+rnd.randint(1, 3)]
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
                'tickets',
                'getCountTickets',
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
                'tickets',
                'getCountTickets',
                json.dumps(
                    {
                        "ids": tickets_id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(offices_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tickets',
                'getCountTickets',
                json.dumps(
                    {
                        "officeIds": [
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
                'tickets',
                'getCountTickets',
                json.dumps(
                    {
                        "officeIds": offices_ids[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
