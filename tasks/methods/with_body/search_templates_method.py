import common_functions.functions as fun
import random as rnd
import json


def search_templates(
        templates_Id,
        users_offices_ids,
        creators_ids,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(templates_Id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchTemplates',
                json.dumps(
                    {
                        "filter": {
                            "ids": [
                                i_number
                            ]
                        }
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchTemplates',
                json.dumps(
                    {
                        "filter": {
                            "ids": templates_Id[i:i+rnd.randint(1, 5)]
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(users_offices_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchTemplates',
                json.dumps(
                    {
                        "filter": {
                            "officesIds": [
                                i_number
                            ]
                        }
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchTemplates',
                json.dumps(
                    {
                        "filter": {
                            "officesIds": users_offices_ids[i:i+rnd.randint(1, 5)]
                        }
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchTemplates',
                json.dumps(
                    {
                        "filter": {
                            "officesIds": users_offices_ids[i:i+rnd.randint(1, 5)],
                            "searchParams": {
                                "limit": rnd.randint(1, 10)
                            }
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*3

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(creators_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchTemplates',
                json.dumps(
                    {
                        "filter": {
                            "creators_ids": [
                                i_number
                            ]
                        }
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchTemplates',
                json.dumps(
                    {
                        "filter": {
                            "creators_ids": creators_ids[i:i+rnd.randint(1, 5)]
                        }
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'tasks',
                'searchTemplates',
                json.dumps(
                    {
                        "filter": {
                            "creators_ids": creators_ids[i:i+rnd.randint(1, 5)]
                        },
                        "searchParams":
                        {
                            "limit": rnd.randint(1, 10)
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*3

    return count_of_request, list_of_ammo
