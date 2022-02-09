from attachments_business.methods import get_attachments_business_data
from attachments_business.methods.with_parameters import get_city_base_count_media_method
from attachments_business.methods.with_parameters import get_object_count_media_method
from attachments_business.methods.with_body import get_files_method
from attachments_business.methods.with_body import get_layouts_by_full_seria_method
from attachments_business.methods.with_body import get_media_for_object_list_method
from attachments_business.methods.with_body_and_parameters import get_media_method
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
    incoming_attachments_business_info = get_attachments_business_data.get_info(
        target,
        currentdir
    )
    objects_id = incoming_attachments_business_info[0]
    general_plans_id = incoming_attachments_business_info[1]
    housing_complexes_id = incoming_attachments_business_info[2]
    entity_id = incoming_attachments_business_info[3]
    attachments_id = incoming_attachments_business_info[4]
    series_general_plans = incoming_attachments_business_info[5]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            get_city_base_count_media_method.get_city_base_count_media,
            objects_id,
            general_plans_id,
            housing_complexes_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_object_count_media_method.get_object_count_media,
            entity_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_files_method.get_files,
            attachments_id,
            entity_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_layouts_by_full_seria_method.get_layouts_by_full_seria,
            series_general_plans,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_media_for_object_list_method.get_media_for_object_list,
            entity_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_media_method.get_media,
            attachments_id,
            entity_id,
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
