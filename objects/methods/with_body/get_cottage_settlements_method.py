import common_functions.functions as fun
import random as rnd
import json


def get_cottage_settlements(
        cottage_settlements_id,
        adresses_id,
        developer_id_cottage_settlements_id,
        road_cottage_settlements_id,
        land_purpose_cottage_settlements_id,
        status_cottage_settlements_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(cottage_settlements_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCottageSettlements',
                json.dumps(
                    {
                        "ids": [
                            i_number
                        ]
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCottageSettlements',
                json.dumps(
                    {
                        "ids": cottage_settlements_id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(adresses_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCottageSettlements',
                json.dumps(
                    {
                        "addressId": [
                            i_number
                        ]
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCottageSettlements',
                json.dumps(
                    {
                        "addressId": adresses_id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(developer_id_cottage_settlements_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCottageSettlements',
                json.dumps(
                    {
                        "developerId": [
                            i_number
                        ]
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCottageSettlements',
                json.dumps(
                    {
                        "developerId": developer_id_cottage_settlements_id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(road_cottage_settlements_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCottageSettlements',
                json.dumps(
                    {
                        "road": [
                            i_number
                        ]
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCottageSettlements',
                json.dumps(
                    {
                        "road": road_cottage_settlements_id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(land_purpose_cottage_settlements_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCottageSettlements',
                json.dumps(
                    {
                        "landPurpose": [
                            i_number
                        ]
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCottageSettlements',
                json.dumps(
                    {
                        "landPurpose": land_purpose_cottage_settlements_id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(status_cottage_settlements_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCottageSettlements',
                json.dumps(
                    {
                        "status": [
                            i_number
                        ]
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCottageSettlements',
                json.dumps(
                    {
                        "status": status_cottage_settlements_id[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
