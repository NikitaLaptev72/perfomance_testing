import common_functions.functions as fun
import random as rnd
import json


def get_objects_with_tickets_for_select(
        offices_id,
        count_of_request,
        duration,
        list_of_ammo
        ):
    ticket_types = [
        1,
        2,
        3,
        4
    ]
    if (count_of_request > duration):
        return count_of_request, list_of_ammo

    for ticket_type in ticket_types:
        for i, i_number in enumerate(offices_id):

            fun.add_to_list(
                list_of_ammo,
                fun.create_req_string_empty_params(
                    'search',
                    'getObjectsWithTicketsForSelect',
                    json.dumps(
                        {
                            "ticketTypes": ticket_type,
                            "officeId": i_number,
                            "limit": rnd.randint(1, 5)
                        },
                        default=str
                    )
                )
            )
    count_of_request += i*len(ticket_types)

    return count_of_request, list_of_ammo
