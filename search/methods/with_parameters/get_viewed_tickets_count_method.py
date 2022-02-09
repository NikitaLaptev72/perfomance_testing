# Нужна аутентификация юзера
import common_functions.functions as fun
import json


def get_viewed_tickets_count(
        users_id,
        сount_of_request,
        duration,
        list_of_ammo
        ):
    if (сount_of_request > duration):
        return сount_of_request, list_of_ammo

    for i, i_number in enumerate(users_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'search',
                'getViewedTicketsCount',
                json.dumps(
                    {
                        "userId": i_number
                    },
                    default=str
                )
            )
        )
    сount_of_request += i

    return сount_of_request, list_of_ammo
