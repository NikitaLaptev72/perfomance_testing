import common_functions.functions as fun
import random as rnd
import json


def get_count_objects(
        object_ids,
        status_object_ids,
        class_object_ids,
        type_object_ids,
        cadastr_object_ids,
        adresses_id,
        personal_account_object_ids,
        new_building_owner_type_object_ids,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(object_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCountObjects',
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
                'getCountObjects',
                json.dumps(
                    {
                        "ids": object_ids[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(status_object_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCountObjects',
                json.dumps(
                    {
                        "statuses": [
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
                'getCountObjects',
                json.dumps(
                    {
                        "statuses": status_object_ids[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(class_object_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCountObjects',
                json.dumps(
                    {
                        "classes": [
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
                'getCountObjects',
                json.dumps(
                    {
                        "classes": class_object_ids[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(type_object_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCountObjects',
                json.dumps(
                    {
                        "types": [
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
                'getCountObjects',
                json.dumps(
                    {
                        "types": type_object_ids[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(cadastr_object_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCountObjects',
                json.dumps(
                    {
                        "cadastres": [
                            i_number
                        ]
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(adresses_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCountObjects',
                json.dumps(
                    {
                        "addressIds": [
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
                'getCountObjects',
                json.dumps(
                    {
                        "addressIds": adresses_id[i:i+rnd.randint(1, 3)]
                    }
                ),
                default=str
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(personal_account_object_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCountObjects',
                json.dumps(
                    {
                        "personalAccounts": [
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
                'getCountObjects',
                json.dumps(
                    {
                        "personalAccounts": personal_account_object_ids[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(new_building_owner_type_object_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'objects',
                'getCountObjects',
                json.dumps(
                    {
                        "newBuildingOwnerTypes": [
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
                'getCountObjects',
                json.dumps(
                    {
                        "newBuildingOwnerTypes": new_building_owner_type_object_ids[
                            i:i+rnd.randint(
                                1,
                                3
                            )
                        ]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
