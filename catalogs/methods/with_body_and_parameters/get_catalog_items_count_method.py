import common_functions.functions as fun
import json


def get_catalog_items_count(
        catalogs_id,
        catalogs_name,
        catalogs_title,
        catalogs_description,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i_catalogs_id, i_number_catalogs_id in enumerate(catalogs_id):
        for i, i_number in enumerate(catalogs_name):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'catalogs',
                    'getCatalogItemsCount',
                    json.dumps(
                        {
                            "catalogId": i_number_catalogs_id
                        },
                        default=str
                    ),
                    json.dumps(
                        [
                            {
                                "field": "name",
                                "op": "like",
                                "value": i_number
                            }
                        ],
                        default=str
                    )
                )
            )

        count_of_request += i

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(catalogs_title):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'catalogs',
                    'getCatalogItemsCount',
                    json.dumps(
                        {
                            "catalogId": i_number_catalogs_id
                        },
                        default=str
                    ),
                    json.dumps(
                        [
                            {
                                "field": "title",
                                "op": "like",
                                "value": i_number
                            }
                        ],
                        default=str
                    )
                )
            )

        count_of_request += i

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(catalogs_description):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'catalogs',
                    'getCatalogItemsCount',
                    json.dumps(
                        {
                            "catalogId": i_number_catalogs_id
                        },
                        default=str
                    ),
                    json.dumps(
                        [
                            {
                                "field": "description",
                                "op": "like",
                                "value": i_number
                            }
                        ],
                        default=str
                    )
                )
            )

        count_of_request += i

    return count_of_request, list_of_ammo
