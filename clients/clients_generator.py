from clients.methods import get_clients_data
from clients.methods.with_parameters import get_clients_with_same_phone_method
from clients.methods.with_parameters import get_realtors_contacts_method
from clients.methods.with_body import count_in_phone_book_method
from clients.methods.with_body import get_agencies_method
from clients.methods.with_body import get_clients_count_method
from clients.methods.with_body import get_clients_method
from clients.methods.with_body import clients_get_fields_values_method
from clients.methods.with_body import get_realtors_count_method
from clients.methods.with_body import get_realtors_method
from clients.methods.with_body import get_realtors_for_export_method
from clients.methods.with_body import search_in_phone_book_method
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
    incoming_clients_info = get_clients_data.get_info(
        target,
        currentdir
    )
    persons_id = incoming_clients_info[0]
    realtors_id = incoming_clients_info[1]
    cities_id = incoming_clients_info[2]
    agencies_id = incoming_clients_info[3]
    contacts_id = incoming_clients_info[4]
    contacts_value = incoming_clients_info[5]
    contacts_type = incoming_clients_info[6]
    realtors_full_name = incoming_clients_info[7]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            get_clients_with_same_phone_method.get_clients_with_same_phone,
            persons_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_realtors_contacts_method.get_realtors_contacts,
            realtors_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            count_in_phone_book_method.count_in_phone_book,
            realtors_id,
            cities_id,
            agencies_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_agencies_method.get_agencies,
            agencies_id,
            cities_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_clients_count_method.get_clients_count,
            persons_id,
            contacts_id,
            contacts_value,
            contacts_type,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_clients_method.get_clients,
            persons_id,
            contacts_id,
            contacts_value,
            contacts_type,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            clients_get_fields_values_method.get_fields_values,
            persons_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_realtors_count_method.get_realtors_count,
            realtors_id,
            cities_id,
            agencies_id,
            realtors_full_name,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_realtors_method.get_realtors,
            realtors_id,
            cities_id,
            agencies_id,
            realtors_full_name,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_realtors_for_export_method.get_realtors_for_export,
            realtors_id,
            cities_id,
            agencies_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_in_phone_book_method.search_in_phone_book,
            realtors_id,
            cities_id,
            agencies_id,
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
