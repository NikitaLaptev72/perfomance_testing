import common_functions.functions as fun
import random as rnd
import json


def search_activities(
        activities_id,
        type_id_activities_id,
        status_id_activities_id,
        description_activities_id,
        start_dateactivities_id,
        end_date_activities_id,
        speaker_activities_fields,
        city_activities_fields,
        for_whom_activities_fields,
        format_activities_fields,
        scale_activities_fields,
        name_activities_fields,
        price_activities_fields,
        where_activities_fields,
        translation_link_activities_fields,
        for_which_city_activities_fields,
        notification_activities_fields,
        result_activities_fields,
        comment_activities_fields,
        topic_activities_fields,
        office_activities_fields,
        entity_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(activities_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activities.id": [
                                i_number
                            ]
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activities.id": activities_id[i:i+rnd.randint(1, 5)]
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(type_id_activities_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activities.typeId": [
                                i_number
                            ]
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activities.typeId": type_id_activities_id[i:i+rnd.randint(1, 5)]
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(status_id_activities_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activities.statusId": [
                                i_number
                            ]
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activities.statusId": status_id_activities_id[i:i+rnd.randint(1, 5)]
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(description_activities_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activities.description": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(start_dateactivities_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activities.startDate": [
                                i_number
                            ]
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(end_date_activities_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activities.endDate": [
                                i_number
                            ]
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(speaker_activities_fields):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activities.speaker": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(city_activities_fields):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activitiesFields.city": [
                                i_number
                            ]
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(for_whom_activities_fields):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activitiesFields.forWhom": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(format_activities_fields):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activitiesFields.format": [
                                i_number
                            ]
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(scale_activities_fields):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activitiesFields.scale": [
                                i_number
                            ]
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(name_activities_fields):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activitiesFields.name": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(price_activities_fields):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activitiesFields.price": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(where_activities_fields):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activitiesFields.where": [
                                i_number
                            ]
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(translation_link_activities_fields):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activitiesFields.translationLink": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(for_which_city_activities_fields):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activitiesFields.forWhichCity": [
                                i_number
                            ]
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(notification_activities_fields):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activitiesFields.notification": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(result_activities_fields):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activitiesFields.result": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(comment_activities_fields):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activitiesFields.comment": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(topic_activities_fields):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activitiesFields.topic": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(office_activities_fields):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "activitiesFields.office": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(entity_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "entities.client": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "entities.ticket": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "entities.hr_demand": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "entities.hr_hiring_ticket": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "entities.hr_candidate_ticket": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "entities.hr_candidate": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "entities.call": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'activities-business',
                'searchActivities',
                json.dumps(
                    {
                        "searchFields": {
                            "entities.responsible": i_number
                        },
                        "searchParams": {
                            "limit": 20,
                            "offset": 0
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i*8

    return count_of_request, list_of_ammo
