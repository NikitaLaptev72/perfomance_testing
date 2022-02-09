import common_functions.functions as fun
import random as rnd
import json


def get_addresses(
        adresses_id,
        adresses_value,
        country_id,
        federal_districts_id,
        regions_id,
        areas_id,
        cities_id,
        settlements_id,
        districts_id,
        streets_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'id',
        'value',
        'unrestrictedValue',
        'postalCode',
        'country_id',
        'federalDistrictId',
        'regionId',
        'areaId',
        'cityId',
        'settlementId',
        'cityDistrictId',
        'streetId',
        'houseFiasId',
        'houseKladrId',
        'houseType',
        'houseTypeFull',
        'house',
        'blockType',
        'blockTypeFull',
        'block',
        'flatType',
        'flatTypeFull',
        'flat',
        'postalBox',
        'fiasId',
        'kladrId',
        'capitalMarker',
        'okato',
        'oktmo',
        'taxOffice',
        'taxOfficeLegal',
        'geoLat',
        'geoLon',
        'timezone'
    ]
    components = [
        'country',
        'federalDistrict',
        'region',
        'area',
        'city',
        'settlement',
        'cityDistrict',
        'street'
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for number_field, field in enumerate(fields):
        for i, i_number in enumerate(adresses_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "ids": i_number,
                            "fields": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "ids": adresses_id[i:i+rnd.randint(1, 5)],
                            "fields": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(adresses_value):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "values": i_number,
                            "fields": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(country_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "countryIds": i_number,
                            "fields": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "countryIds": country_id[i:i+rnd.randint(1, 5)],
                            "fields": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(federal_districts_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "federalDistrictIds": i_number,
                            "fields": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "federalDistrictIds": federal_districts_id[i:i+rnd.randint(1, 5)],
                            "fields": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(regions_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "regionIds": i_number,
                            "fields": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "regionIds": regions_id[i:i+rnd.randint(1, 5)],
                            "fields": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(areas_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "areaIds": i_number,
                            "fields": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "areaIds": areas_id[i:i+rnd.randint(1, 5)],
                            "fields": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(cities_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "cityIds": i_number,
                            "fields": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "cityIds": cities_id[i:i+rnd.randint(1, 5)],
                            "fields": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(settlements_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "settlementIds": i_number,
                            "fields": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "settlementIds": settlements_id[i:i+rnd.randint(1, 5)],
                            "fields": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(districts_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "cityDistrictIds": i_number,
                            "fields": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "cityDistrictIds": districts_id[i:i+rnd.randint(1, 5)],
                            "fields": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(streets_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "streetIds": i_number,
                            "fields": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "streetIds": streets_id[i:i+rnd.randint(1, 5)],
                            "fields": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

    for number_field, field in enumerate(components):
        for i, i_number in enumerate(adresses_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "ids": i_number,
                            "fields": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "ids": adresses_id[i:i+rnd.randint(1, 5)],
                            "fields": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(adresses_value):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "values": i_number,
                            "components": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(country_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "countryIds": i_number,
                            "components": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "values": country_id[i:i+rnd.randint(1, 5)],
                            "components": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(federal_districts_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "federalDistrictIds": i_number,
                            "components": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "federalDistrictIds": federal_districts_id[i:i+rnd.randint(1, 5)],
                            "components": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(regions_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "regionIds": i_number,
                            "components": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "regionIds": regions_id[i:i+rnd.randint(1, 5)],
                            "components": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(areas_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "areaIds": i_number,
                            "components": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "areaIds": areas_id[i:i+rnd.randint(1, 5)],
                            "components": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(cities_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "cityIds": i_number,
                            "components": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "areaIds": cities_id[i:i+rnd.randint(1, 5)],
                            "components": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(settlements_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "settlementIds": i_number,
                            "components": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "cityIds": settlements_id[i:i+rnd.randint(1, 5)],
                            "components": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(districts_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "cityDistrictIds": i_number,
                            "components": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "cityDistrictIds": districts_id[i:i+rnd.randint(1, 5)],
                            "components": field
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

        if (count_of_request > duration):
            return count_of_request, list_of_ammo

        for i, i_number in enumerate(streets_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "streetIds": i_number,
                            "components": field
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddresses',
                    json.dumps(
                        {
                            "streetIds": i_number,
                            "components": streets_id[i:i+rnd.randint(1, 5)]
                        },
                        default=str
                    )
                )
            )

        count_of_request += i*2

    return count_of_request, list_of_ammo
