import common_functions.functions as fun
import random as rnd
import json


def search_users(
        users_contacts_value,
        users_full_name,
        users_id,
        offices_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    for i, i_number in enumerate(users_contacts_value):
        if (fun.is_email(i_number)):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'users',
                    'searchUsers',
                    json.dumps(
                        {
                            "searchBy": {
                                "email": i_number
                            }
                        },
                        default=str
                    )
                )
            )
        else:
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'users',
                    'searchUsers',
                    json.dumps(
                        {
                            "searchBy": {
                                "phone": i_number
                            }
                        },
                        default=str
                    )
                )
            )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(users_full_name):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'users',
                'searchUsers',
                json.dumps(
                    {
                        "searchBy": {
                            "fullName": i_number
                        }
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
                'users',
                'searchUsers',
                json.dumps(
                    {
                        "searchBy": {
                            "ids": [
                                i_number
                            ]
                        }
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'users',
                'searchUsers',
                json.dumps(
                    {
                        "searchBy": {
                            "ids": users_id[i:i+rnd.randint(1, 5)]
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(offices_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'users',
                'searchUsers',
                json.dumps(
                    {
                        "searchBy": {
                            "ids": [
                                i_number
                            ]
                        }
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'users',
                'searchUsers',
                json.dumps(
                    {
                        "searchBy": {
                            "ids": offices_id[i:i+rnd.randint(1, 5)]
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
