from objects.methods import get_objects_data
from objects.methods.with_parameters import get_cottage_settlement_method
from objects.methods.with_body import get_cottage_settlements_method
from objects.methods.with_body import get_count_objects_method
from objects.methods.with_body import get_entrances_method
from objects.methods.with_body import get_general_plans_method
from objects.methods.with_body import get_history_keys_method
from objects.methods.with_body import get_housing_complexes_method
from objects.methods.with_body import get_installment_terms_method
from objects.methods.with_body import get_keys_method
from objects.methods.with_body import get_objects_method
from objects.methods.with_body import get_promotions_method
from objects.methods.with_body_and_parameters import get_object_fields_values_method
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
    incoming_objects_info = get_objects_data.get_info(
        target,
        currentdir
    )
    cottage_settlements_id = incoming_objects_info[0]
    adresses_id = incoming_objects_info[1]
    developer_id_cottage_settlements_id = incoming_objects_info[2]
    road_cottage_settlements_id = incoming_objects_info[3]
    land_purpose_cottage_settlements_id = incoming_objects_info[4]
    status_cottage_settlements_id = incoming_objects_info[5]
    object_ids = incoming_objects_info[6]
    status_object_ids = incoming_objects_info[7]
    class_object_ids = incoming_objects_info[8]
    type_object_ids = incoming_objects_info[9]
    cadastr_object_ids = incoming_objects_info[10]
    personal_account_object_ids = incoming_objects_info[11]
    new_building_owner_type_object_ids = incoming_objects_info[12]
    entrances_id = incoming_objects_info[13]
    general_plan_entrances_id = incoming_objects_info[14]
    general_plans_id = incoming_objects_info[15]
    housing_complex_general_plans_id = incoming_objects_info[16]
    history_keys_id = incoming_objects_info[17]
    keys_id_history_keys_id = incoming_objects_info[18]
    housing_complexes_id = incoming_objects_info[19]
    developer_housing_complexes_id = incoming_objects_info[20]
    general_plans_installment_terms_id = incoming_objects_info[21]
    keys_id = incoming_objects_info[22]
    promotions_id = incoming_objects_info[23]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            get_cottage_settlement_method.get_cottage_settlement,
            cottage_settlements_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_cottage_settlements_method.get_cottage_settlements,
            cottage_settlements_id,
            adresses_id,
            developer_id_cottage_settlements_id,
            road_cottage_settlements_id,
            land_purpose_cottage_settlements_id,
            status_cottage_settlements_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_count_objects_method.get_count_objects,
            object_ids,
            status_object_ids,
            class_object_ids,
            type_object_ids,
            cadastr_object_ids,
            adresses_id,
            personal_account_object_ids,
            new_building_owner_type_object_ids,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_entrances_method.get_entrances,
            entrances_id,
            general_plan_entrances_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_general_plans_method.get_general_plans,
            general_plans_id,
            adresses_id,
            housing_complex_general_plans_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_history_keys_method.get_history_keys,
            history_keys_id,
            object_ids,
            keys_id_history_keys_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_housing_complexes_method.get_housing_complexes,
            housing_complexes_id,
            developer_housing_complexes_id,
            adresses_id, count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_installment_terms_method.get_installment_terms,
            general_plans_installment_terms_id,
            general_plans_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_keys_method.get_keys,
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_objects_method.getObjects,
            keys_id,
            object_ids,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_promotions_method.get_promotions,
            promotions_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_object_fields_values_method.get_object_fields_values,
            object_ids,
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
