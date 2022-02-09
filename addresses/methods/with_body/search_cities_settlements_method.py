import common_functions.functions as fun
import json


def search_cities_settlements(
        city_mame,
        cities_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(city_mame):
        for j, j_number in enumerate(cities_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'searchCitiesSettlements',
                    json.dumps(
                        {
                            "filter": [
                                {
                                    "field": "name",
                                    "op": "ilike",
                                    "value": i_number
                                }
                            ],
                            "ids": [
                                {
                                    "entity": "city",
                                    "entityId": j_number
                                }
                            ]
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*j

    return count_of_request, list_of_ammo
