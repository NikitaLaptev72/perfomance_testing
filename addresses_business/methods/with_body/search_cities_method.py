import common_functions.functions as fun
import json


def search_cities(
        city_name,
        count_of_request,
        duration,
        list_of_ammo
        ):
    for i, i_number in enumerate(city_name):

        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses-business',
                'searchCities',
                json.dumps(
                    {
                        "search": [
                            i_number
                        ]
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    return count_of_request, list_of_ammo
