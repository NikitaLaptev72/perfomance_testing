import common_functions.functions as fun
import random as rnd
import json


def get_activity_fields_values(
        activities_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'activities.createdAt',
        'activities.description',
        'activities.endDate',
        'activities.id',
        'activities.isMassEvent',
        'activities.startDate',
        'activities.statusId',
        'activities.typeId'
    ]

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(activities_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_with_parameters_body(
                'activities',
                'getActivityFieldsValues',
                json.dumps(
                    {
                        "activityId": i_number
                    },
                    default=str
                ),
                json.dumps(
                    [
                        rnd.choice(fields)
                    ],
                    default=str
                )
            )
        )

    count_of_request += i

    return count_of_request, list_of_ammo
