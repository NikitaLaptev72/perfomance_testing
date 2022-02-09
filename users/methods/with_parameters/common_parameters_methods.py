import common_functions.functions as fun
import json


def common_parameters(
        users_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(users_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'users',
                'getLinks',
                json.dumps(
                    {
                        "reqUserId": i_number,
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'users',
                'getAdditionals',
                json.dumps(
                    {
                        "requestedUserId": i_number,
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'users',
                'getUser',
                json.dumps(
                    {
                        "requestedUserId": i_number,
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'users',
                'getUserRelationships',
                json.dumps(
                    {
                        "requestedUserId": i_number,
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'users',
                'getUserRoles',
                json.dumps(
                    {
                        "requestedUserId": i_number,
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'users',
                'getUserOffices',
                json.dumps(
                    {
                        "requestedUserId": i_number,
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'users',
                'getUserDepartment',
                json.dumps(
                    {
                        "requestedUserId": i_number,
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'users',
                'getUserGroups',
                json.dumps(
                    {
                        "requestedUserId": i_number,
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'users',
                'getUserContacts',
                json.dumps(
                    {
                        "requestedUserId": i_number,
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'users',
                'getUserSettings',
                json.dumps(
                    {
                        "requestedUserId": i_number,
                    },
                    default=str
                )
            )
        )

    count_of_request += i*10

    return count_of_request, list_of_ammo
