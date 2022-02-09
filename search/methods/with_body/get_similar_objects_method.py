# Метод работает неправильно, т.к. при любых параметрах падает ошибка: None schemas are valid
import common_functions.functions as fun
import random as rnd
import json


def get_similar_objects(
        regions_id,
        cities_id,
        streets_id,
        class_object_ids,
        type_object_ids,
        areas_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for k, k_number in enumerate(class_object_ids):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'search',
                'getSimilarObjects',
                json.dumps(
                    {
                        "regionId": rnd.choice(regions_id),
                        "cityId": rnd.choice(cities_id),
                        "streetId": rnd.choice(streets_id),
                        "object": {
                            "class": k_number,
                            "type": rnd.choice(type_object_ids),
                            "area": rnd.choice(areas_id)
                        }
                    },
                    default=str
                )
            )
        )
    count_of_request += k

    return count_of_request, list_of_ammo
