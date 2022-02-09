import common_functions.functions as fun
import json


def get_confirm(
        activities_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(activities_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_body(
                'activities',
                'getConfirm',
                json.dumps(
                    {
                        "activityId": i_number
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    return count_of_request, list_of_ammo
