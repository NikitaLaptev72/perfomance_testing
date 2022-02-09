import common_functions.functions as fun
import json


def get_address(
        adresses_id,
        adresses_value,
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
                    'getAddress',
                    json.dumps(
                        {
                            "id": i_number,
                            "fields": field
                        },
                        default=str
                    )
                )
            )

        for i, i_number in enumerate(adresses_value):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddress',
                    json.dumps(
                        {
                            "value": i_number,
                            "fields": field
                        },
                        default=str
                    )
                )
            )

    for number_field, field in enumerate(components):
        for i, i_number in enumerate(adresses_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddress',
                    json.dumps(
                        {
                            "id": i_number,
                            "components": field
                        },
                        default=str
                    )
                )
            )

        for i, i_number in enumerate(adresses_value):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'addresses',
                    'getAddress',
                    json.dumps(
                        {
                            "value": i_number,
                            "components": field
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*4

    return count_of_request, list_of_ammo
