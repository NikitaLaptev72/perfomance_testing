import common_functions.functions as fun
import json


def get_user_count(
        users_id,
        offices_id,
        users_contacts_value,
        users_full_name,
        count_of_request,
        duration,
        list_of_ammo,
        departments_id
        ):
    op = [
        '=',
        '!=',
        '<>',
        '>',
        '>=',
        '<',
        '<='
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for j, j_number in enumerate(op):
        for i, i_number in enumerate(users_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'users',
                    'getUserCount',
                    json.dumps(
                        {
                            "filter": [
                                {
                                    "field": "id",
                                    "op": j_number,
                                    "value": i_number
                                }
                            ]
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*j

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for k, k_number in enumerate(departments_id):
        for j, j_number in enumerate(op):
            for i, i_number in enumerate(users_id):
                fun.add_to_list(
                    list_of_ammo,
                    fun.create_req_string_empty_params(
                        'users',
                        'getUserCount',
                        json.dumps(
                            {
                                "filter": [
                                    {
                                        "field": "id",
                                        "op": j_number,
                                        "value": i_number
                                    }
                                ],
                                "searchBy": {
                                    "departmentId": k_number
                                }
                            },
                            default=str
                        )
                    )
                )

    count_of_request += i*j*k

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for k, k_number in enumerate(offices_id):
        for j, j_number in enumerate(op):
            for i, i_number in enumerate(users_id):
                fun.add_to_list(
                    list_of_ammo,
                    fun.create_req_string_empty_params(
                        'users',
                        'getUserCount',
                        json.dumps(
                            {
                                "filter": [
                                    {
                                        "field": "id",
                                        "op": j_number,
                                        "value": i_number
                                    }
                                ],
                                "searchBy": {
                                    "officeIds": k_number
                                }
                            },
                            default=str
                        )
                    )
                )

    count_of_request += i*j*k

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for k, k_number in enumerate(users_contacts_value):
        for j, j_number in enumerate(op):
            for i, i_number in enumerate(users_id):
                if fun.is_email(k_number):
                    fun.add_to_list(
                        list_of_ammo,
                        fun.create_req_string_empty_params(
                            'users',
                            'getUserCount',
                            json.dumps(
                                {
                                    "filter": [
                                        {
                                            "field": "id",
                                            "op": j_number,
                                            "value": i_number
                                        }
                                    ],
                                    "searchBy": {
                                        "email": k_number
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
                            'getUserCount',
                            json.dumps(
                                {
                                    "filter": [
                                        {
                                            "field": "id",
                                            "op": j_number,
                                            "value": i_number
                                        }
                                    ],
                                    "searchBy": {
                                        "phone": k_number
                                    }
                                },
                                default=str
                            )
                        )
                    )

    count_of_request += i*j*k

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for k, k_number in enumerate(users_full_name):
        for j, j_number in enumerate(op):
            for i, i_number in enumerate(users_id):
                fun.add_to_list(
                    list_of_ammo,
                    fun.create_req_string_empty_params(
                        'users',
                        'getUserCount',
                        json.dumps(
                            {
                                "filter": [
                                    {
                                        "field": "id",
                                        "op": j_number,
                                        "value": i_number
                                    }
                                ],
                                "searchBy": {
                                    "fullName": k_number
                                }
                            },
                            default=str
                        )
                    )
                )

    count_of_request += i*j*k

    return count_of_request, list_of_ammo
