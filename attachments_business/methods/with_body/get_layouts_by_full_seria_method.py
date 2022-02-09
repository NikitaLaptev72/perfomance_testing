import common_functions.functions as fun
import json
import random as rnd


def get_layouts_by_full_seria(
        series_general_plans,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(series_general_plans):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'attachments-business',
                'getLayoutsByFullSeria',
                json.dumps(
                    {
                        "seria": i_number,
                        "limit": rnd.randint(
                            10,
                            20
                        )
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    return count_of_request, list_of_ammo
