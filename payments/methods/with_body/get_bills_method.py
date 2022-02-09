import common_functions.functions as fun
import json
import random as rnd


def get_bills(
        bills_id,
        bills_balance,
        bills_limit,
        bills_type,
        bills_status,
        users_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'id',
        'userId',
        'balance'
    ]
    operators = [
        '=',
        '!=',
        '>',
        '>=',
        '<',
        '<='
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for operator in operators:
        for i, i_number in enumerate(bills_id):

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'payments',
                    'getBills',
                    json.dumps(
                        {
                            "fields": [
                                rnd.choice(fields)
                            ],
                            "filter": [
                                {
                                    "field": "id",
                                    "operation": operator,
                                    "value": i_number
                                }
                            ]
                        },
                        default=str
                    )
                )
            )

        count_of_request += i

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(bills_balance):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'payments',
                    'getBills',
                    json.dumps(
                        {
                            "fields": [
                                rnd.choice(fields)
                            ],
                            "filter": [
                                {
                                    "field": "balance",
                                    "operation": operator,
                                    "value": i_number
                                }
                            ]
                        },
                        default=str
                    )
                )
            )

        count_of_request += i

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(bills_limit):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'payments',
                    'getBills',
                    json.dumps(
                        {
                            "fields": [
                                rnd.choice(fields)
                            ],
                            "filter": [
                                {
                                    "field": "limit",
                                    "operation": operator,
                                    "value": i_number
                                }
                            ]
                        },
                        default=str
                    )
                )
            )

        count_of_request += i

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(bills_type):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'payments',
                    'getBills',
                    json.dumps(
                        {
                            "fields": [
                                rnd.choice(fields)
                            ],
                            "filter": [
                                {
                                    "field": "type",
                                    "operation": operator,
                                    "value": i_number
                                }
                            ]
                        },
                        default=str
                    )
                )
            )

        count_of_request += i

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(bills_status):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'payments',
                    'getBills',
                    json.dumps(
                        {
                            "fields": [
                                rnd.choice(fields)
                            ],
                            "filter": [
                                {
                                    "field": "status",
                                    "operation": operator,
                                    "value": i_number
                                }
                            ]
                        },
                        default=str
                    )
                )
            )

        count_of_request += i

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(users_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'payments',
                    'getBills',
                    json.dumps(
                        {
                            "fields": [
                                rnd.choice(fields)
                            ],
                            "filter": [
                                {
                                    "field": "userId",
                                    "operation": operator,
                                    "value": i_number
                                }
                            ]
                        },
                        default=str
                    )
                )
            )

        count_of_request += i

    return count_of_request, list_of_ammo
