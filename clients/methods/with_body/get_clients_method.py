import common_functions.functions as fun
import random as rnd
import json


def get_clients(
        persons_id,
        contacts_id,
        contacts_value,
        contacts_type,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'id',
        'clientType',
        'createdAt',
        'fullName',
        'data',
        'fieldsValues',
        'contacts',
        'relations',
        'clientsCompaniesRelations'
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for field in fields:
        for i, i_number in enumerate(persons_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'clients',
                    'getClients',
                    json.dumps(
                        {
                            "ids": [
                                i_number
                            ],
                            "fields": [
                                field
                            ]
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'clients',
                    'getClients',
                    json.dumps(
                        {
                            "ids": persons_id[i:i+rnd.randint(1, 3)],
                            "fields": [
                                field
                            ]
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(contacts_id):
            if (count_of_request > duration):
                return count_of_request, list_of_ammo

            fun.add_to_list(
                list_of_ammo, fun.create_req_string_empty_params(
                    'clients',
                    'getClients',
                    json.dumps(
                        {
                            "contacts":
                            {
                                "ids": [
                                    i_number
                                ]
                            },
                            "fields": [
                                field
                            ]
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo, fun.create_req_string_empty_params(
                    'clients',
                    'getClients',
                    json.dumps(
                        {
                            "contacts":
                            {
                                "ids": contacts_id[i:i+rnd.randint(1, 3)]
                            },
                            "fields": [
                                field
                            ]
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(contacts_type):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'clients',
                    'getClients',
                    json.dumps(
                        {
                            "contacts":
                            {
                                "types": [
                                    i_number
                                ]
                            },
                            "fields": [
                                field
                            ]
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'clients',
                    'getClients',
                    json.dumps(
                        {
                            "contacts":
                            {
                                "types": contacts_type[i:i+rnd.randint(1, 3)]
                            },
                            "fields": [
                                field
                            ]
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(contacts_value):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'clients',
                    'getClients',
                    json.dumps(
                        {
                            "contacts":
                            {
                                "value": i_number
                            },
                            "fields": [
                                field
                            ]
                        },
                        default=str
                    )
                )
            )

        count_of_request += i

    return count_of_request, list_of_ammo
