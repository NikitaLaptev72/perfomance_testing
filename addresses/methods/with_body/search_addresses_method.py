import common_functions.functions as fun
import json


def search_addresses(
        adresses_value,
        count_of_request,
        duration,
        list_of_ammo
        ):
    from_bound = [
        'country',
        'region',
        'area',
        'city',
        'settlement',
        'street',
        'house'
    ]
    to_bound = [
        'country',
        'region',
        'area',
        'city',
        'settlement',
        'street',
        'house'
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(adresses_value):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'searchAddresses',
                json.dumps(
                    {
                        "value": i_number
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(from_bound):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'searchAddresses',
                json.dumps(
                    {
                        "fromBound": i_number
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(to_bound):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'searchAddresses',
                json.dumps(
                    {
                        "toBound": i_number
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(adresses_value):
        for j, j_number in enumerate(from_bound):
            for k, k_number in enumerate(to_bound):
                fun.add_to_list(
                    list_of_ammo,
                    fun.create_req_string_empty_params(
                        'addresses',
                        'searchAddresses',
                        json.dumps(
                            {
                                "value": i_number,
                                "toBound": j_number,
                                "fromBound": k_number
                            },
                            default=str
                        )
                    )
                )

    count_of_request += i*j*k

    return count_of_request, list_of_ammo
