from tickets.methods import get_tickets_data
from tickets.methods.with_parameters import get_ticket_bu_method
from tickets.methods.with_body import get_clients_realtors_count_method
from tickets.methods.with_body import get_count_tickets_method
from tickets.methods.with_body import get_tickets_method
from tickets.methods.with_body_and_parameters import get_ticket_fields_values_method
import concurrent.futures
import common_functions.functions as fun


def generate_ammo_method(
        target,
        count_of_request,
        duration,
        example_file,
        list_of_ammo,
        currentdir
        ):
    incoming_tickets_info = get_tickets_data.get_info(
        target,
        currentdir
    )
    tickets_id = incoming_tickets_info[0]
    сlients_id = incoming_tickets_info[1]
    offices_ids = incoming_tickets_info[2]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            get_ticket_bu_method.get_ticket_bu,
            tickets_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_clients_realtors_count_method.get_clients_realtors_count,
            сlients_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_count_tickets_method.get_count_tickets,
            сlients_id,
            tickets_id,
            offices_ids,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_tickets_method.get_tickets,
            сlients_id,
            tickets_id,
            offices_ids,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_ticket_fields_values_method.get_ticket_fields_values,
            tickets_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        fun.write_list_to_file(
            example_file,
            list_of_ammo
        )

        return count_of_request
