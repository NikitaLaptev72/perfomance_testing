from catalogs_business.methods import get_catalogs_business_data
from catalogs_business.methods.with_parameters import get_catalog_items_method
from catalogs_business.methods.with_parameters import get_client_fields_method
from catalogs_business.methods.with_parameters import get_feedback_widget_fields_method
from catalogs_business.methods.with_parameters import get_task_creation_fields_method
from catalogs_business.methods.with_body import get_activity_fields_method
from catalogs_business.methods.with_body import get_cancel_reasons_method

    
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
    incoming_catalogs_business_data = get_catalogs_business_data.get_info(
        target,
        currentdir
    )
    catalogs_id = incoming_catalogs_business_data[0]
    tasks_category_id = incoming_catalogs_business_data[1]
    tickets_type_id = incoming_catalogs_business_data[2]
    office_id = incoming_catalogs_business_data[3]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            get_catalog_items_method.get_catalog_items,
            catalogs_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        # # future = executor.submit(
        # #     get_client_fields_method.get_client_fields,
        # #     count_of_request,
        # #     duration,
        # #     list_of_ammo
        # # )
        # # count_of_request, list_of_ammo = future.result()

        # # future = executor.submit(
        # #     get_feedback_widget_fields_method.get_feedback_widget_fields,
        # #     tasks_category_id,
        # #     count_of_request,
        # #     duration,
        # #     list_of_ammo
        # # )
        # # count_of_request, list_of_ammo = future.result()

        # # future = executor.submit(
        # #     get_task_creation_fields_method.get_task_creation_fields,
        # #     count_of_request,
        # #     duration,
        # #     list_of_ammo
        # # )
        # # count_of_request, list_of_ammo = future.result()

        # # future = executor.submit(
        # #     get_activity_fields_method.get_activity_fields,
        # #     count_of_request,
        # #     duration,
        # #     list_of_ammo
        # # )
        # # count_of_request, list_of_ammo = future.result()

        # future = executor.submit(
        #     get_cancel_reasons_method.get_cancel_reasons,
        #     tickets_type_id,
        #     office_id,
        #     count_of_request,
        #     duration,
        #     list_of_ammo
        # )
        # count_of_request, list_of_ammo = future.result()

        fun.write_list_to_file(
            example_file,
            list_of_ammo
        )

        return count_of_request