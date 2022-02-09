import common_functions.functions as fun
import json


def get_city_base_count_media(
        objects_id,
        general_plans_id,
        housing_complexes_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(objects_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'attachments-business',
                'getCityBaseCountMedia',
                json.dumps(
                    {
                        "objectId": i_number
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(general_plans_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'attachments-business',
                'getCityBaseCountMedia',
                json.dumps(
                    {
                        "gpId": i_number
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(housing_complexes_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'attachments-business',
                'getCityBaseCountMedia',
                json.dumps(
                    {
                        "hcId": i_number
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    return count_of_request, list_of_ammo
