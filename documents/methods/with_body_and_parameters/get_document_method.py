import common_functions.functions as fun
import random as rnd
import json


def get_document(
        documents_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'id',
        'typeId',
        'userId',
        'name',
        'archivedAt',
        'archiverId',
        'createdAt'
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(documents_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_with_parameters_body(
                'documents',
                'getDocument',
                json.dumps(
                    {
                        "documentId": i_number
                    },
                    default=str
                ),
                json.dumps(
                    {
                        {
                            "fields": [
                                rnd.choice(fields)
                            ]
                        }
                    },
                    default=str
                )
            )
        )
    count_of_request += i

    return count_of_request, list_of_ammo
