import common_functions.functions as fun
import json


def get_count_layouts_by_full_seria(
        general_plans_series,
        сount_of_request,
        duration,
        list_of_ammo
        ):
    if (сount_of_request > duration):
        return сount_of_request, list_of_ammo

    for i, i_number in enumerate(general_plans_series):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'search',
                'getCountLayoutsByFullSeria',
                json.dumps(
                    {
                        "seria": i_number
                    },
                    default=str
                )
            )
        )
    сount_of_request += i

    return сount_of_request, list_of_ammo
