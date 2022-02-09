import common_functions.functions
import random as rnd
import json


def search_documents(
        documents_id,
        users_id,
        documents_type_id,
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
        common_functions.functions.writing_to_file(
            list_of_ammo,
            common_functions.functions.create_req_string_empty_params(
                'documents',
                'searchDocuments',
                json.dumps(
                    {
                        "filter":
                        {
                            "ids": [
                                i_number
                            ]
                        },
                        "params": {
                            "fields": [
                                rnd.choice(fields)
                            ]
                        }
                    },
                    default=str
                )
            )
        )
        common_functions.functions.writing_to_file(
            list_of_ammo,
            common_functions.functions.create_req_string_empty_params(
                'documents',
                'searchDocuments',
                json.dumps(
                    {
                        "filter":
                        {
                            "ids": documents_id[i:i+rnd.randint(1, 5)]
                        },
                        "params": {
                            "fields": [
                                rnd.choice(fields)
                            ]
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
        common_functions.functions.writing_to_file(
            list_of_ammo,
            common_functions.functions.create_req_string_empty_params(
                'documents',
                'searchDocuments',
                json.dumps(
                    {
                        "filter":
                        {
                            "usersIds": [
                                i_number
                            ]
                        },
                        "params": {
                            "fields": [
                                rnd.choice(fields)
                            ]
                        }
                    },
                    default=str
                )
            )
        )
        common_functions.functions.writing_to_file(
            list_of_ammo,
            common_functions.functions.create_req_string_empty_params(
                'documents',
                'searchDocuments',
                json.dumps(
                    {
                        "filter":
                        {
                            "usersIds": users_id[i:i+rnd.randint(1, 5)]
                        },
                        "params": {
                            "fields": [
                                rnd.choice(fields)
                            ]
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
        common_functions.functions.writing_to_file(
            list_of_ammo,
            common_functions.functions.create_req_string_empty_params(
                'documents',
                'searchDocuments',
                json.dumps(
                    {
                        "filter":
                        {
                            "typesIds": [
                                i_number
                            ]
                        },
                        "params": {
                            "fields": [
                                rnd.choice(fields)
                            ]
                        }
                    },
                    default=str
                )
            )
        )
        common_functions.functions.writing_to_file(
            list_of_ammo,
            common_functions.functions.create_req_string_empty_params(
                'documents',
                'searchDocuments',
                json.dumps(
                    {
                        "filter":
                        {
                            "typesIds": documents_type_id[i:i+rnd.randint(1, 5)]
                        },
                        "params": {
                            "fields": [
                                rnd.choice(fields)
                            ]
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
