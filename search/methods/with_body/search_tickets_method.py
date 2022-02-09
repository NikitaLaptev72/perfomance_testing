import common_functions.functions as fun
import random as rnd
import json


def search_tickets(
        tickets_id,
        users_id,
        offices_id,
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
                'search',
                'searchTickets',
                json.dumps(
                    {
                        "filter": {
                            "ticketsIds": [
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
                'search',
                'searchTickets',
                json.dumps(
                    {
                        "filter": {
                            "ticketsIds": tickets_id[i:i+rnd.randint(1, 5)]
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(users_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'searchTickets',
                json.dumps(
                    {
                        "filter": {
                            "userIds": [
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
                'search',
                'searchTickets',
                json.dumps(
                    {
                        "filter": {
                            "userIds": users_id[i:i+rnd.randint(1, 5)]
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(offices_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'searchTickets',
                json.dumps(
                    {
                        "filter": {
                            "officeIds": [
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
                'search',
                'searchTickets',
                json.dumps(
                    {
                        "filter": {
                            "officeIds": offices_id[i:i+rnd.randint(1, 5)]
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
