import common_functions.functions as fun
import json


def get_clients_with_same_phone(
        persons_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(persons_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'clients',
                'getClientsWithSamePhone',
                json.dumps(
                    {
                        "clientId": i_number
                    },
                    default=str
                )
            )
        )
    count_of_request += i

    return count_of_request, list_of_ammo
