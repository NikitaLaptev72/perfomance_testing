import common_functions.functions as fun
import random as rnd
import json


def get_fields_values(
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
            fun.create_req_string_empty_params(
                'clients',
                'getFieldsValues',
                json.dumps(
                    [
                        i_number
                    ],
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'clients',
                'getFieldsValues',
                json.dumps(
                    persons_id[i:i+rnd.randint(1, 3)],
                    default=str
                )
            )
        )
    count_of_request += i*2

    return count_of_request, list_of_ammo
