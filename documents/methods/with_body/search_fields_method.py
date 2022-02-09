import common_functions.functions as fun
import random as rnd
import json


def search_fields(
        documents_id,
        documents_type_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(documents_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'documents',
                'searchFields',
                json.dumps(
                    {
                        "filter":
                        {
                            "documentsIds": [
                                i_number
                            ]
                        },
                        "params": {
                            "limit": 10
                        }
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'documents',
                'searchFields',
                json.dumps(
                    {
                        "filter":
                        {
                            "documentsIds": documents_id[i:i+rnd.randint(1, 5)]
                        },
                        "params": {
                            "limit": 10
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(documents_type_id):
        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'documents',
                'searchFields',
                json.dumps(
                    {
                        "filter":
                        {
                            "typesIds": [
                                i_number
                            ]
                        },
                        "params": {
                            "limit": 10
                        }
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'documents',
                'searchFields',
                json.dumps(
                    {
                        "filter":
                        {
                            "typesIds": documents_type_id[i:i+rnd.randint(1, 5)]
                        },
                        "params": {
                            "limit": 10
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
