import common_functions.functions as fun
import json


def get_entities_activities_dates(
        entity_id,
        entity,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(entity_id):
        for j, j_number in enumerate(entity):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'activities',
                    'getEntitiesActivitiesDates',
                    json.dumps(
                        [
                            {
                                "entity_id": i_number,
                                "entity": j_number
                            }
                        ],
                        default=str
                    )
                )
            )

    count_of_request += i

    return count_of_request, list_of_ammo
