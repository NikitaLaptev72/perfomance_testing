import common_functions.functions as fun
import json


def get_catalog_item_ids_by_uuids(
        uuid_catalog_items,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(uuid_catalog_items):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_with_parameters_body(
                'catalogs',
                'getCatalogItemIdsByUuids',
                json.dumps(
                    {
                        "field": "id"
                    },
                    default=str
                ),
                json.dumps(
                    {
                        "group":
                        [
                            i_number
                        ]
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    return count_of_request, list_of_ammo
