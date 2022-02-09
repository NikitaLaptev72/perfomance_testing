import common_functions.functions as fun
import random as rnd
import json


def search_temp_entities(
        tasks_id,
        entities_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    entities = [
        2,
        3,
        4,
        5
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for entity in entities:
        for i, i_number in enumerate(tasks_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'tasks',
                    'searchTempEntities',
                    json.dumps(
                        {
                            "tasksIds": [
                                i_number
                            ],
                            "entity": entity
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'tasks',
                    'searchTempEntities',
                    json.dumps(
                        {
                            "tasksIds": tasks_id[i:i+rnd.randint(1, 5)],
                            "entity": entity
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(entities_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'tasks',
                    'searchTempEntities',
                    json.dumps(
                        {
                            "entitiesIds": [
                                i_number
                            ],
                            "entity": entity
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'tasks',
                    'searchTempEntities',
                    json.dumps(
                        {
                            "entitiesIds": entities_id[i:i+rnd.randint(1, 5)],
                            "entity": entity
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

    return count_of_request, list_of_ammo
