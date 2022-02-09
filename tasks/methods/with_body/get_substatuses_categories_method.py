import common_functions.functions as fun
import json


def get_substatuses_categories(
        sub_statuses_names,
        offices_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(offices_id):
        for j, j_number in enumerate(sub_statuses_names):

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'tasks',
                    'getSubstatusesCategories',
                    json.dumps(
                        {
                            "name": j_number,
                            "officeId": i_number
                        },
                        default=str
                    )
                )
            )
    count_of_request += i*j

    return count_of_request, list_of_ammo
