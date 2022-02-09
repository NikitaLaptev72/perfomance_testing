import common_functions.functions as fun
import random as rnd
import json


def get_attachments(
        attachmentsId,
        attachmentsname,
        relationsentity,
        relationsentityId,
        count_of_request,
        duration,
        list_of_ammo
        ):
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(attachmentsId):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'attachments',
                'getAttachments',
                json.dumps(
                    {
                        "ids": i_number
                    },
                    default=str
                )
            )
        )

        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'attachments',
                'getAttachments',
                json.dumps(
                    {
                        "ids": attachmentsId[i:i+rnd.randint(1, 3)]
                    },
                    default=str
                )
            )
        )

    count_of_request += i*2

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(attachmentsname):
        fun.add_to_list(
            list_of_ammo,
            fun.create_req_string_empty_params(
                'attachments',
                'getAttachments',
                json.dumps(
                    {
                        "name": i_number
                    },
                    default=str
                )
            )
        )

    count_of_request += i

    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for i, i_number in enumerate(relationsentity):
        for j, j_number in enumerate(relationsentityId):
            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'attachments',
                    'getAttachments',
                    json.dumps(
                        {
                            "relations": [
                                {
                                    "entity": i_number,
                                    "entityId": j_number
                                }
                            ],
                            "limit": rnd.randint(1, 5)
                        },
                        default=str
                    )
                )
            )

    count_of_request += i

    return count_of_request, list_of_ammo
