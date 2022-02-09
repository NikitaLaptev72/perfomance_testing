from search.methods import get_search_data
from search.methods.with_parameters import get_count_layouts_by_full_seria_method
from search.methods.with_parameters import get_viewed_tickets_count_method
from search.methods.with_body import get_layouts_by_full_seria_method
from search.methods.with_body import get_objects_with_tickets_for_select_method
from search.methods.with_body import get_only_tickets_by_stages_method
from search.methods.with_body import get_only_tickets_count_by_stages_method
from search.methods.with_body import get_only_tickets_count_method
from search.methods.with_body import get_only_tickets_method
from search.methods.with_body import get_shows_method
from search.methods.with_body import get_count_shows_method
from search.methods.with_body import get_similar_objects_method
from search.methods.with_body import get_tickets_by_object_method
from search.methods.with_body import search_tickets_method
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
    incoming_search_info = get_search_data.get_info(
        target,
        currentdir
    )
    general_plans_series = incoming_search_info[0]
    users_id = incoming_search_info[1]
    offices_id = incoming_search_info[2]
    tickets_id = incoming_search_info[3]
    tickets_alternative_stages = incoming_search_info[4]
    tickets_stages = incoming_search_info[5]
    cities_id = incoming_search_info[6]
    realtors_id = incoming_search_info[7]
    contacts_id = incoming_search_info[8]
    addresses_id = incoming_search_info[9]
    shows_id = incoming_search_info[10]
    object_ids = incoming_search_info[11]
    regions_id = incoming_search_info[12]
    streets_id = incoming_search_info[13]
    areas_id = incoming_search_info[14]
    class_object_ids = incoming_search_info[15]
    type_object_ids = incoming_search_info[16]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            get_count_layouts_by_full_seria_method.get_count_layouts_by_full_seria,
            general_plans_series,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_viewed_tickets_count_method.get_viewed_tickets_count,
            users_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_layouts_by_full_seria_method.get_layouts_by_full_seria,
            general_plans_series,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_objects_with_tickets_for_select_method.get_objects_with_tickets_for_select,
            offices_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_only_tickets_by_stages_method.get_only_tickets_by_stages,
            tickets_id,
            tickets_alternative_stages,
            tickets_stages,
            cities_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_only_tickets_count_by_stages_method.get_only_tickets_count_by_stages,
            tickets_id,
            tickets_stages,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_only_tickets_count_method.get_only_tickets_count,
            tickets_id,
            tickets_stages,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_only_tickets_method.get_only_tickets,
            tickets_id,
            tickets_stages,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_shows_method.get_shows,
            users_id,
            realtors_id,
            contacts_id,
            addresses_id,
            shows_id,
            tickets_id,
            object_ids,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_count_shows_method.get_count_shows,
            users_id,
            realtors_id,
            contacts_id,
            addresses_id,
            shows_id,
            tickets_id,
            object_ids,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        # Метод работает неправильно
        future = executor.submit(
            get_similar_objects_method.get_similar_objects,
            regions_id,
            cities_id,
            streets_id,
            class_object_ids,
            type_object_ids,
            areas_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_tickets_by_object_method.get_tickets_by_object,
            users_id,
            object_ids,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_tickets_method.search_tickets,
            tickets_id,
            users_id,
            offices_id,
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
