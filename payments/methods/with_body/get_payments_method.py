import common_functions.functions as fun
import random as rnd
import json


def get_payments(
        payments_id,
        bills_id,
        payments_bill_from,
        paymentsbill_to,
        payments_amount,
        users_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'id',
        'billFrom',
        'billTo',
        'amount'
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

    generated_fields = fun.combinations(fields)
    generated_fields.pop(0)

    for field in generated_fields:
        for operator in operators:
            for i, i_number in enumerate(payments_id):
                fun.add_to_list(
                    list_of_ammo,
                    fun.create_req_string_empty_params(
                        'payments',
                        'getPayments',
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
                            }
                        )
                    )
                )

            count_of_request += i

            if (count_of_request > duration):
                return count_of_request, list_of_ammo

            for i, i_number in enumerate(bills_id):
                fun.add_to_list(
                    list_of_ammo,
                    fun.create_req_string_empty_params(
                        'payments',
                        'getPayments',
                        json.dumps(
                            {
                                "fields": [
                                    rnd.choice(fields)
                                ],
                                "filter": [
                                    {
                                        "field": "billId",
                                        "operation": operator,
                                        "value": i_number
                                    }
                                ]
                            }
                        )
                    )
                )

            count_of_request += i

            if (count_of_request > duration):
                return count_of_request, list_of_ammo

            for i, i_number in enumerate(payments_bill_from):
                fun.add_to_list(
                    list_of_ammo,
                    fun.create_req_string_empty_params(
                        'payments',
                        'getPayments',
                        json.dumps(
                            {
                                "fields": [
                                    rnd.choice(fields)
                                ],
                                "filter": [
                                    {
                                        "field": "billFrom",
                                        "operation": operator,
                                        "value": i_number
                                    }
                                ]
                            }
                        )
                    )
                )

            count_of_request += i

            if (count_of_request > duration):
                return count_of_request, list_of_ammo

            for i, i_number in enumerate(paymentsbill_to):
                fun.add_to_list(
                    list_of_ammo,
                    fun.create_req_string_empty_params(
                        'payments',
                        'getPayments',
                        json.dumps(
                            {
                                "fields": [
                                    rnd.choice(fields)
                                ],
                                "filter": [
                                    {
                                        "field": "billTo",
                                        "operation": operator,
                                        "value": i_number
                                    }
                                ]
                            }
                        )
                    )
                )

            count_of_request += i

            if (count_of_request > duration):
                return count_of_request, list_of_ammo

            for i, i_number in enumerate(payments_amount):
                fun.add_to_list(
                    list_of_ammo,
                    fun.create_req_string_empty_params(
                        'payments',
                        'getPayments',
                        json.dumps(
                            {
                                "fields": [
                                    rnd.choice(fields)
                                ],
                                "filter": [
                                    {
                                        "field": "amount",
                                        "operation": operator,
                                        "value": i_number
                                    }
                                ]
                            }
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
                        'getPayments',
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
                            }
                        )
                    )
                )

            count_of_request += i

    return count_of_request, list_of_ammo
