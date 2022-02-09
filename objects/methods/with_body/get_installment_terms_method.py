import common_functions.functions as fun
import random as rnd
import json


def get_installment_terms(
        general_plans_installment_terms_id,
        general_plans_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'id',
        'generalPlanId',
        'title',
        'description'
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for j, j_number in enumerate(fields):
        for i, i_number in enumerate(general_plans_installment_terms_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'objects',
                    'getInstallmentTerms',
                    json.dumps(
                        {
                            "fields": [
                                j_number
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
                    'objects',
                    'getInstallmentTerms',
                    json.dumps(
                        {
                            "fields": [
                                j_number
                            ],
                            "ids": general_plans_installment_terms_id[i:i+rnd.randint(1, 3)]
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*j*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for j, j_number in enumerate(fields):
        for i, i_number in enumerate(general_plans_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'objects',
                    'getInstallmentTerms',
                    json.dumps(
                        {
                            "fields": [
                                j_number
                            ],
                            "generalPlanIds": [
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
                    'objects',
                    'getInstallmentTerms',
                    json.dumps(
                        {
                            "fields": [
                                j_number
                            ],
                            "generalPlanIds": general_plans_id[i:i+rnd.randint(1, 3)]
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*j*2

    return count_of_request, list_of_ammo
