import common_functions.functions as fun
import random as rnd
import json


def get_tickets_by_object(
        users_id,
        object_ids,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(users_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getOnlyTickets',
                json.dumps(
                    {
                        "userId": i_number,
                        "objectIdSearch": rnd.choice(object_ids)
                    },
                    default=str
                )
            )
        )
    count_of_request += i

    return count_of_request, list_of_ammo
