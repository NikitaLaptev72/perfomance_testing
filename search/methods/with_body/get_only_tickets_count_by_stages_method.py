import common_functions.functions as fun
import random as rnd
import json


def get_only_tickets_count_by_stages(
            tickets_id,
            tickets_stages,
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
                'getOnlyTicketsCountByStages',
                json.dumps(
                    {
                        "tickets.id": [
                            i_number
                        ],
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
                'getOnlyTicketsCountByStages',
                json.dumps(
                    {
                        "tickets.id": tickets_id[i:i+rnd.randint(1, 3)],
                        "isAlternativeStage": True
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(ticket_types):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getOnlyTicketsCountByStages',
                json.dumps(
                    {
                        "tickets.typeId": [
                            i_number
                        ],
                        "isAlternativeStage": True
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
                'getOnlyTicketsCountByStages',
                json.dumps(
                    {
                        "tickets.stageId": [
                            i_number
                        ],
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
                'getOnlyTicketsCountByStages',
                json.dumps(
                    {
                        "tickets.stageId": tickets_stages[i:i+rnd.randint(1, 3)],
                        "isAlternativeStage": True
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
