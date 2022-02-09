import common_functions.functions as fun
import json


def get_catalog(
        catalogs_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(catalogs_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'catalogs',
                'getCatalog',
                json.dumps(
                    {
                        "catalogId": i_number
                    },
                    default=str
                )
            )
        )
    count_of_request += i

    return count_of_request, list_of_ammo