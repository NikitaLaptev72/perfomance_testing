import common_functions.functions as fun
import random as rnd
import json


def get_cities(
        cities_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'id',
        'cityName',
        'countryId',
        'regionId',
        'areaId',
        'cityFiasId',
        'cityKladrId',
        'cityWithType',
        'cityType',
        'cityTypeFull',
        'createdAt'
    ]
    generated_fields = fun.combinations(
        fields
    )
    generated_fields.pop(0)

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(cities_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'getCities',
                json.dumps(
                    {
                        "ids": i_number,
                        "fields": rnd.choice(generated_fields)
                    },
                    default=str
                )
            )
        )
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'getCities',
                json.dumps(
                    {
                        "ids": cities_id[i:i+rnd.randint(1, 5)],
                        "fields": rnd.choice(generated_fields)
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    return count_of_request, list_of_ammo
