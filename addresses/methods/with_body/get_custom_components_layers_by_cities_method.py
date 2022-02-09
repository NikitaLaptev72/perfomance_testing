import common_functions.functions as fun
import random as rnd
import json


def get_custom_Components_layers_by_cities(
        cities_id,
        districts_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(cities_id):
        for j, j_number in enumerate(districts_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getCustomComponentsLayersByCities',
                    json.dumps(
                        {
                            "cities": [
                                {
                                    "entity": "city",
                                    "entityId": i_number
                                }
                            ],
                            "districtIds": [
                                j_number
                            ]
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getCustomComponentsLayersByCities',
                    json.dumps(
                        {
                            "cities": [
                                {
                                    "entity": "city",
                                    "entityId": i_number
                                }
                            ],
                            "districtIds": [
                                districts_id[j:j+rnd.randint(1, 5)]
                            ]
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*2

    return count_of_request, list_of_ammo
