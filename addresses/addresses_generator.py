from addresses.methods import get_addresses_data
from addresses.methods.with_parameters import get_metro_by_address_method
from addresses.methods.with_body import get_addresses_method
from addresses.methods.with_body import get_address_method
from addresses.methods.with_body import get_cities_method
from addresses.methods.with_body import get_custom_components_layers_by_cities_method
from addresses.methods.with_body import get_districts_method
from addresses.methods.with_body import get_streets_method
from addresses.methods.with_body import search_addresses_method
from addresses.methods.with_body import search_cities_settlements_method
from addresses.methods.with_body import search_components_method
from addresses.methods.with_body import search_streets_by_patches_method
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
    incoming_addresses_info = get_addresses_data.get_info(
        target,
        currentdir
    )
    adresses_id = incoming_addresses_info[0]
    adresses_value = incoming_addresses_info[1]
    country_id = incoming_addresses_info[2]
    federal_districts_id = incoming_addresses_info[3]
    regions_id = incoming_addresses_info[4]
    areas_id = incoming_addresses_info[5]
    cities_id = incoming_addresses_info[6]
    settlements_id = incoming_addresses_info[7]
    districts_id = incoming_addresses_info[8]
    streets_id = incoming_addresses_info[9]
    city_name = incoming_addresses_info[10]
    patch_id = incoming_addresses_info[11]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            get_metro_by_address_method.get_metro_by_address,
            adresses_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_addresses_method.get_addresses,
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
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_address_method.get_address,
            adresses_id,
            adresses_value,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_cities_method.get_cities,
            cities_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_custom_components_layers_by_cities_method.get_custom_Components_layers_by_cities,
            cities_id,
            districts_id,
            count_of_request,
            duration, list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_districts_method.get_districts,
            cities_id,
            districts_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_streets_method.get_streets,
            cities_id,
            districts_id,
            streets_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_addresses_method.search_addresses,
            adresses_value,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_cities_settlements_method.search_cities_settlements,
            city_name,
            cities_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_components_method.search_components,
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
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_streets_by_patches_method.search_streets_by_patches,
            patch_id,
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
        )
        count_of_request, list_of_ammo = future.result()

        fun.write_list_to_file(
            example_file,
            list_of_ammo
        )

    return count_of_request
