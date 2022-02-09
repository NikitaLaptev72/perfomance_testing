import common_functions.functions as fun
import random as rnd
import json


def get_activity_fields_values(
        activities_id,
        start_dateactivities_id,
        end_date_activities_id,
        type_id_activities_id,
        speaker_activities_fields,
        city_activities_fields,
        format_activities_fields,
        name_activities_fields,
        description_activities_id,
        price_activities_fields,
        translation_link_activities_fields,
        result_activities_fields,
        comment_activities_fields,
        topic_activities_fields,
        count_of_request,
        duration,
        list_of_ammo
        ):
    target_fields = [
        7, 12, 36
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for target_field in target_fields:
        for i, i_number in enumerate(activities_id):

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'activities-business',
                    'getActivityFields',
                    json.dumps(
                        {
                            "activityId": i_number,
                            'targetFields': target_field
                        },
                        default=str
                    ),
                    json.dumps(
                        {
                            "activities.startDate": rnd.choice(start_dateactivities_id)
                        },
                        default=str
                    )
                )
            )

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'activities-business',
                    'getActivityFields',
                    json.dumps(
                        {
                            "activityId": i_number,
                            'targetFields': target_field
                        },
                        default=str
                    ),
                    json.dumps(
                        {
                            "activities.endDate": rnd.choice(end_date_activities_id)
                        },
                        default=str
                    )
                )
            )

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'activities-business',
                    'getActivityFields',
                    json.dumps(
                        {
                            "activityId": i_number,
                            'targetFields': target_field
                        },
                        default=str
                    ),
                    json.dumps(
                        {
                            "activities.typeId": rnd.choice(type_id_activities_id)
                        },
                        default=str
                    )
                )
            )

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'activities-business',
                    'getActivityFields',
                    json.dumps(
                        {
                            "activityId": i_number,
                            'targetFields': target_field
                        },
                        default=str
                    ),
                    json.dumps(
                        {
                            "activitiesFields.speaker": rnd.choice(speaker_activities_fields)
                        },
                        default=str
                    )
                )
            )

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'activities-business',
                    'getActivityFields',
                    json.dumps(
                        {
                            "activityId": i_number,
                            'targetFields': target_field
                        },
                        default=str
                    ),
                    json.dumps(
                        {
                            "activitiesFields.city": rnd.choice(city_activities_fields)
                        },
                        default=str
                    )
                )
            )

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'activities-business',
                    'getActivityFields',
                    json.dumps(
                        {
                            "activityId": i_number,
                            'targetFields': target_field
                        },
                        default=str
                    ),
                    json.dumps(
                        {
                            "activitiesFields.format": rnd.choice(format_activities_fields)
                        },
                        default=str
                    )
                )
            )

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'activities-business',
                    'getActivityFields',
                    json.dumps(
                        {
                            "activityId": i_number,
                            'targetFields': target_field
                        },
                        default=str
                    ),
                    json.dumps(
                        {
                            "activitiesFields.name": rnd.choice(name_activities_fields)
                        },
                        default=str
                    )
                )
            )

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'activities-business',
                    'getActivityFields',
                    json.dumps(
                        {
                            "activityId": i_number,
                            'targetFields': target_field
                        },
                        default=str
                    ),
                    json.dumps(
                        {
                            "activitiesFields.description": rnd.choice(description_activities_id)
                        },
                        default=str
                    )
                )
            )

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'activities-business',
                    'getActivityFields',
                    json.dumps(
                        {
                            "activityId": i_number,
                            'targetFields': target_field
                        },
                        default=str
                    ),
                    json.dumps(
                        {
                            "activitiesFields.price": rnd.choice(price_activities_fields)
                        },
                        default=str
                    )
                )
            )

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'activities-business',
                    'getActivityFields',
                    json.dumps(
                        {
                            "activityId": i_number,
                            'targetFields': target_field
                        },
                        default=str
                    ),
                    json.dumps(
                        {
                            "activitiesFields.translationLink": rnd.choice(
                                translation_link_activities_fields
                            )
                        },
                        default=str
                    )
                )
            )

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'activities-business',
                    'getActivityFields',
                    json.dumps(
                        {
                            "activityId": i_number,
                            'targetFields': target_field
                        },
                        default=str
                    ),
                    json.dumps(
                        {
                            "activitiesFields.result": rnd.choice(result_activities_fields)
                        },
                        default=str
                    )
                )
            )

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'activities-business',
                    'getActivityFields',
                    json.dumps(
                        {
                            "activityId": i_number,
                            'targetFields': target_field
                        },
                        default=str
                    ),
                    json.dumps(
                        {
                            "activitiesFields.comment": rnd.choice(comment_activities_fields)
                        },
                        default=str
                    )
                )
            )

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_with_parameters_body(
                    'activities-business',
                    'getActivityFields',
                    json.dumps(
                        {
                            "activityId": i_number,
                            'targetFields': target_field
                        },
                        default=str
                    ),
                    json.dumps(
                        {
                            "activitiesFields.topic": rnd.choice(topic_activities_fields)
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*13

    return count_of_request, list_of_ammo
