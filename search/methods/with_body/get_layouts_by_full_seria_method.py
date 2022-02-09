import common_functions.functions as fun
import random as rnd
import json


def get_layouts_by_full_seria(
        general_plans_series,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(general_plans_series):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getLayoutsByFullSeria',
                json.dumps(
                    {
                        "seria": i_number,
                        "limit": rnd.randint(1, 5)
                    },
                    default=str
                )
            )
        )
    count_of_request += i

    return count_of_request, list_of_ammo
