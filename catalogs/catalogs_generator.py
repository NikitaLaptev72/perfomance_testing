from catalogs.methods import get_catalogs_data
from catalogs.methods.with_parameters import get_catalog_items_method
from catalogs.methods.with_parameters import get_catalog_method
from catalogs.methods.with_parameters import get_catalogs_params_method
from catalogs.methods.with_body import get_catalogs_count_method
from catalogs.methods.with_body import search_catalogs_method
from catalogs.methods.with_body_and_parameters import get_catalog_item_ids_by_uuids_method
from catalogs.methods.with_body_and_parameters import get_catalog_items_count_method
from catalogs.methods.with_body_and_parameters import search_in_catalog_method
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
    incoming_catalogs_info = get_catalogs_data.get_info(
        target,
        currentdir
    )
    catalogs_id = incoming_catalogs_info[0]
    catalogs_name = incoming_catalogs_info[1]
    catalogs_title = incoming_catalogs_info[2]
    catalogs_description = incoming_catalogs_info[3]
    uuid_catalog_items = incoming_catalogs_info[4]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            get_catalog_items_method.get_catalog_items,
            catalogs_id,
            count_of_request,
            duration, list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_catalog_method.get_catalog,
            catalogs_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_catalogs_params_method.get_catalogs_params,
            catalogs_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_catalogs_count_method.get_catalogs_count,
            catalogs_id,
            catalogs_name,
            catalogs_title,
            catalogs_description,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_catalogs_method.search_catalogs,
            catalogs_id,
            catalogs_name,
            catalogs_title,
            catalogs_description,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_catalog_item_ids_by_uuids_method.get_catalog_item_ids_by_uuids,
            uuid_catalog_items,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_catalog_items_count_method.get_catalog_items_count,
            catalogs_id,
            catalogs_name,
            catalogs_title,
            catalogs_description,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_in_catalog_method.search_in_catalog,
            catalogs_id,
            catalogs_name,
            catalogs_title,
            catalogs_description,
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
