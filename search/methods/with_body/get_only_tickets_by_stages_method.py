import common_functions.functions as fun
import random as rnd
import json


def get_only_tickets_by_stages(
        tickets_id,
        tickets_alternative_stages,
        tickets_stages,
        cities_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    ticket_types = [
        1,
        2,
        3,
        4
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(tickets_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getOnlyTicketsByStages',
                json.dumps(
                    {
                        "filter": {
                            "tickets.id": [
                                i_number
                            ]
                        },
                        "isAlternativeStage": True
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getOnlyTicketsByStages',
                json.dumps(
                    {
                        "filter": {
                            "tickets.id": tickets_id[i:i+rnd.randint(1, 3)]
                        },
                        "isAlternativeStage": True
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(ticket_types):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getOnlyTicketsByStages',
                json.dumps(
                    {
                        "filter": {
                            "tickets.id": [
                                i_number
                            ]
                        },
                        "isAlternativeStage": True,
                        "limit": rnd.randint(5, 15)
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(tickets_stages):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getOnlyTicketsByStages',
                json.dumps(
                    {
                        "filter": {
                            "tickets.stageId": [
                                i_number
                            ]
                        },
                        "isAlternativeStage": True,
                        "limit": rnd.randint(5, 15)
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getOnlyTicketsByStages',
                json.dumps(
                    {
                        "filter": {
                            "tickets.stageId": tickets_stages[i:i+rnd.randint(1, 3)]
                        },
                        "isAlternativeStage": True,
                        "limit": rnd.randint(5, 15)
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(tickets_alternative_stages):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getOnlyTicketsByStages',
                json.dumps(
                    {
                        "filter": {
                            "tickets.alternativeStageId": [
                                i_number
                            ]
                        },
                        "isAlternativeStage": True,
                        "limit": rnd.randint(5, 15)
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getOnlyTicketsByStages',
                json.dumps(
                    {
                        "filter": {
                            "tickets.alternativeStageId": tickets_alternative_stages[
                                i:i+rnd.randint(
                                    1,
                                    3
                                )
                            ]
                        },
                        "isAlternativeStage": True,
                        "limit": rnd.randint(5, 15)
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
                'search',
                'getOnlyTicketsByStages',
                json.dumps(
                    {
                        "filter": {
                            "tickets.cityId": [
                                i_number
                            ]
                        },
                        "isAlternativeStage": True,
                        "limit": rnd.randint(5, 15)
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getOnlyTicketsByStages',
                json.dumps(
                    {
                        "filter": {
                            "tickets.cityId": cities_id[i:i+rnd.randint(1, 3)]
                        },
                        "isAlternativeStage": True,
                        "limit": rnd.randint(5, 15)
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
