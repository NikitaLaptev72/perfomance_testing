import common_functions.functions as fun
import json


def search_components(
        country_id,
        federal_districts_id,
        regions_id,
        areas_id,
        cities_id,
        settlements_id,
        districts_id,
        streets_id,
        city_name,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(country_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'searchComponents',
                json.dumps(
                    {
                        "component": "street",
                        "searchParams": {
                            "filter": [
                                {
                                    "field": "id",
                                    "op": "=",
                                    "value": i_number
                                }
                            ],
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(federal_districts_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'searchComponents',
                json.dumps(
                    {
                        "component": "federalDistrict",
                        "searchParams": {
                            "filter": [
                                {
                                    "field": "id",
                                    "op": "=",
                                    "value": i_number
                                }
                            ],
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(regions_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'searchComponents',
                json.dumps(
                    {
                        "component": "region",
                        "searchParams": {
                            "filter": [
                                {
                                    "field": "id",
                                    "op": "=",
                                    "value": i_number
                                }
                            ],
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(areas_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'searchComponents',
                json.dumps(
                    {
                        "component": "area",
                        "searchParams": {
                            "filter": [
                                {
                                    "field": "id",
                                    "op": "=",
                                    "value": i_number
                                }
                            ],
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(cities_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'searchComponents',
                json.dumps(
                    {
                        "component": "city",
                        "searchParams": {
                            "filter": [
                                {
                                    "field": "id",
                                    "op": "=",
                                    "value": i_number
                                }
                            ],
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(city_name):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'searchComponents',
                json.dumps(
                    {
                        "component": "city",
                        "searchParams": {
                            "filter": [
                                {
                                    "field": "city_name",
                                    "op": "like",
                                    "value": i_number
                                }
                            ],
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(settlements_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'searchComponents',
                json.dumps(
                    {
                        "component": "settlement",
                        "searchParams": {
                            "filter": [
                                {
                                    "field": "id",
                                    "op": "=",
                                    "value": i_number
                                }
                            ],
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(districts_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'searchComponents',
                json.dumps(
                    {
                        "component": "cityDistrict",
                        "searchParams": {
                            "filter": [
                                {
                                    "field": "id",
                                    "op": "=",
                                    "value": i_number
                                }
                            ],
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(streets_id):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'addresses',
                'searchComponents',
                json.dumps(
                    {
                        "component": "street",
                        "searchParams": {
                            "filter": [
                                {
                                    "field": "id",
                                    "op": "=",
                                    "value": i_number
                                }
                            ],
                        }
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    return count_of_request, list_of_ammo
