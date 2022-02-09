import common_functions.functions as fun
import json


def get_user_contact(
        users_contacts_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(users_contacts_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'users',
                'getUserContact',
                json.dumps(
                    {
                        "contactId": i_number,
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    return count_of_request, list_of_ammo
