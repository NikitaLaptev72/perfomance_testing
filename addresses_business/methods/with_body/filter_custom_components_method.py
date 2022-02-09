import common_functions.functions as fun
import json


def filter_custom_components(
        patch_entity,
        patch_entity_id,
        patch_layer_id,
        patch_id,
        streets_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    for i, i_number in enumerate(patch_entity):
        for j, j_number in enumerate(patch_entity_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses-business',
                    'filterCustomComponents',
                    json.dumps(
                        {
                            "OR": [
                                {
                                    "patchEntities": [
                                        {
                                            "patchEntity": i_number,
                                            "patchEntityId": j_number
                                        }
                                    ]
                                }
                            ]
                        },
                        default=str
                    )
                )
            )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(patch_layer_id):

        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses-business',
                'filterCustomComponents',
                json.dumps(
                    {
                        "OR": [
                            {
                                "patchLayerIds": [
                                    i_number
                                ]
                            }
                        ]
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(patch_id):

        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses-business',
                'filterCustomComponents',
                json.dumps(
                    {
                        "OR": [
                            {
                                "patchesIds": [
                                    i_number
                                ]
                            }
                        ]
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(streets_id):

        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses-business',
                'filterCustomComponents',
                json.dumps(
                    {
                        "OR": [
                            {
                                "streetIds": [
                                    i_number
                                ]
                            }
                        ]
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    return count_of_request, list_of_ammo
