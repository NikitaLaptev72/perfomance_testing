from addresses_business.methods import get_addresses_business_data
from addresses_business.methods.with_body import filter_custom_components_method
from addresses_business.methods.with_body import get_default_components_method
from addresses_business.methods.with_body import get_offices_in_cities_method
from addresses_business.methods.with_body import search_cities_method
from addresses_business.methods.with_body import search_cities_with_offices_method
from addresses_business.methods.with_body import search_dependent_addresses_method
from addresses_business.methods.with_parameters import get_country_method
from addresses_business.methods.with_parameters import get_offices_in_city_method
from addresses_business.methods.with_parameters import get_offices_in_settlement_method
from addresses_business.methods.with_parameters import get_offices_without_city_of_appeal_method
from addresses_business.methods.with_parameters import get_custom_components_city_layers_method
from addresses_business.methods.with_body_and_parameters import get_off_by_address_entities_method
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
    incoming_addresses_info = get_addresses_business_data.get_info(
        target,
        currentdir
    )
    adresses_id = incoming_addresses_info[0]
    country_id = incoming_addresses_info[2]
    regions_id = incoming_addresses_info[4]
    areas_id = incoming_addresses_info[5]
    cities_id = incoming_addresses_info[6]
    settlements_id = incoming_addresses_info[7]
    districts_id = incoming_addresses_info[8]
    streets_id = incoming_addresses_info[9]
    city_name = incoming_addresses_info[10]
    patch_id = incoming_addresses_info[11]
    patch_entity = incoming_addresses_info[12]
    patch_entity_id = incoming_addresses_info[13]
    patch_layer_id = incoming_addresses_info[14]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            get_country_method.get_country,
            country_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_offices_in_city_method.get_offices_in_city,
            cities_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_offices_in_settlement_method.get_offices_in_settlement,
            settlements_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_offices_without_city_of_appeal_method.get_offices_without_city_of_appeal,
            adresses_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_custom_components_city_layers_method.get_custom_components_city_layers_settings,
            patch_entity_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            filter_custom_components_method.filter_custom_components,
            patch_entity,
            patch_entity_id,
            patch_layer_id,
            patch_id,
            streets_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_off_by_address_entities_method.get_offices_by_address_entities,
            patch_entity_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_default_components_method.get_default_components,
            regions_id,
            areas_id,
            cities_id,
            settlements_id,
            districts_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_offices_in_cities_method.get_offices_in_cities,
            cities_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_cities_method.search_cities,
            city_name,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_cities_with_offices_method.search_cities_with_offices,
            city_name,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_dependent_addresses_method.search_dependent_addresses,
            adresses_id,
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

        fun.write_list_to_file(
            example_file,
            list_of_ammo
        )

    return count_of_request
