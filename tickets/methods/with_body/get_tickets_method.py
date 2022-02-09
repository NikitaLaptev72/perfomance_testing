import common_functions.functions as fun
import random as rnd
import json


def get_tickets(
        clients_id,
        tickets_id,
        offices_ids,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'title',
        'status',
        'type',
        'office',
        'source',
        'createdAt',
        'desc',
        'realtorDesc',
        'selfDesc',
        'auction',
        'endDate',
        'internal',
        'sourcesDetail',
        'transferred',
        'regional',
        'deferred',
        'object', 'values',
        'members',
        'stage',
        'alternativeStage',
        'urgentSale',
        'youngFamily',
        'allInclusive',
        'clientReadiness',
        'reasonOfCancel',
        'temporaryObjectTypeId',
        'notificationOfRegionalTicket'
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for index_field, field in enumerate(fields):
        for i, i_number in enumerate(clients_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'tickets',
                    'getTickets',
                    json.dumps(
                        {
                            "fields": [
                                field
                            ],
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
                    'getTickets',
                    json.dumps(
                        {
                            "fields": [
                                field
                            ],
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
                    'getTickets',
                    json.dumps(
                        {
                            "fields": [
                                field
                            ],
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
                    'getTickets',
                    json.dumps(
                        {
                            "fields": [
                                field
                            ],
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
                    'getTickets',
                    json.dumps(
                        {
                            "fields": [
                                field
                            ],
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
                    'getTickets',
                    json.dumps(
                        {
                            "fields": [
                                field
                            ],
                            "officeIds": offices_ids[i:i+rnd.randint(1, 3)]
                        },
                        default=str
                    )
                )
            )
        count_of_request += i*2

    return count_of_request, list_of_ammo
