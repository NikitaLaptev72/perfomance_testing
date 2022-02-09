import common_functions.functions as fun
import random as rnd
import json


def get_general_plans(
        general_plans_id,
        adresses_id,
        housing_complex_general_plans_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    fields = [
        'id',
        'name',
        'housingComplexId',
        'addressId',
        'hasOffices',
        'bicycle',
        'concierge',
        'elevator',
        'numFloors',
        'prams',
        'utilityRooms',
        'engineering',
        'yearConstruct',
        'wall',
        'series',
        'yard',
        'dogWalkingArea',
        'houseWear',
        'ownBoiler',
        'uninhabitedPremiseOnFirstFloor',
        'isNewBuilding',
        'cadastr',
        'deadlineYear',
        'deadlineQuarter',
        'salesStart',
        'desc',
        'isShownOnSite',
        'isShownOnList',
        'isClosed',
        'developer',
        'namePD',
        'addressDDU',
        'crossingStreets',
        'geoLat',
        'geoLon',
        'projectDeclarationLink',
        'projectDeclarationLinkADS',
        'houseNumberAvito',
        'houseNumberCian',
        'housingComplexNumberCian',
        'houseNumberYandex',
        'housingComplexNumberYandex',
        'buildingStartQuarter',
        'buildingStartYear',
        'keep',
        'windows',
        'hasMortgage',
        'isYoungFamily',
        'tradeIn',
        'hasSocialPrograms',
        'area',
        'areaFlats',
        'areaLand',
        'numParking',
        'facade',
        'numLivingFloors',
        'numEntrances',
        'numFlats',
        'ceilingHeight',
        'playground',
        'inPlayground',
        'rampant',
        'hasCommunications',
        'hasWaterCounters',
        'hasHeatCounters',
        'hasBalconsGlazing',
        'hasStoreroom',
        'hasIronDoor',
        'hasIntercom',
        'hasVideoIntercom',
        'hasFireAlarm',
        'hasSecurityAlarm',
        'hasClosedYard',
        'hasBarrier',
        'hasGates',
        'hasSecurity',
        'hasVideoSurveillance',
        'hasSportsGround',
        'hasBikeLane',
        'hasParking',
        'parking',
        'hasElevator',
        'isOldElite',
        'company',
        'email',
        'factAddressId',
        'receptionPhone',
        'emergencyPhone',
        'site',
        'category',
        'offices',
        'garages',
        'entrances',
        'flats',
        'characteristic'
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for j, j_number in enumerate(fields):
        for i, i_number in enumerate(general_plans_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'objects',
                    'getGeneralPlans',
                    json.dumps(
                        {
                            "fields": [
                                j_number
                            ],
                            "ids": [
                                i_number
                            ]
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'objects',
                    'getGeneralPlans',
                    json.dumps(
                        {
                            "fields": [
                                j_number
                            ],
                            "ids": general_plans_id[i:i+rnd.randint(1, 3)]
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*j

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for j, j_number in enumerate(fields):
        for i, i_number in enumerate(adresses_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'objects',
                    'getGeneralPlans',
                    json.dumps(
                        {
                            "fields": [
                                j_number
                            ],
                            "addressIds": [
                                i_number
                            ]
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'objects',
                    'getGeneralPlans',
                    json.dumps(
                        {
                            "fields": [
                                j_number
                            ],
                            "addressIds": adresses_id[i:i+rnd.randint(1, 3)]
                        },
                        default=str
                    )
                )
            )
            count_of_request += 2

    count_of_request += i*j

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for j, j_number in enumerate(fields):
        for i, i_number in enumerate(housing_complex_general_plans_id):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'objects',
                    'getGeneralPlans',
                    json.dumps(
                        {
                            "fields": [
                                j_number
                            ],
                            "housingComplexIds": [
                                i_number
                            ]
                        },
                        default=str
                    )
                )
            )
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'objects',
                    'getGeneralPlans',
                    json.dumps(
                        {
                            "fields": [
                                j_number
                            ],
                            "housingComplexIds": housing_complex_general_plans_id[
                                i:i+rnd.randint(
                                    1,
                                    3
                                )
                            ]
                        },
                        default=str
                    )
                )
            )

    count_of_request += i*j

    return count_of_request, list_of_ammo
