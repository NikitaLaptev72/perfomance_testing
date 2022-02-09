from users.methods import get_users_data
from users.methods.with_parameters import common_parameters_methods
from users.methods.with_parameters import get_user_contact_method
from users.methods.with_parameters import get_role_rights_method
from users.methods.with_parameters import get_role_method
from users.methods.with_parameters import get_position_method
from users.methods.with_parameters import get_department_method
from users.methods.with_parameters import get_group_users_count_method
from users.methods.with_parameters import get_group_users_ids_method
from users.methods.with_body import search_departments_method
from users.methods.with_body import search_users_method
from users.methods.with_body import get_upper_hierarchy_method
from users.methods.with_body import get_users_departments_method
from users.methods.with_body import get_users_groups_method
from users.methods.with_body import get_positions_method
from users.methods.with_body import get_user_count_method
from users.methods.with_body import search_user_contacts_method
from users.methods.with_body import search_user_settings_method
from users.methods.with_body import search_ui_setting_method
from users.methods.with_body import search_roles_method
from users.methods.with_body import search_positions_method
from users.methods.with_body import get_office_users_method
from users.methods.with_body import search_groups_method
from users.methods.with_body import get_groups_count_method
from users.methods.with_body_and_parameters import get_group_method
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
    incoming_users_info = get_users_data.get_info(
        target,
        currentdir
    )
    users_full_name = incoming_users_info[0]
    users_contacts_value = incoming_users_info[1]
    users_contacts_id = incoming_users_info[2]
    users_id = incoming_users_info[3]
    roles_id = incoming_users_info[4]
    positions_id = incoming_users_info[5]
    offices_id = incoming_users_info[6]
    departments_id = incoming_users_info[7]
    groups_id = incoming_users_info[8]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            common_parameters_methods.common_parameters,
            users_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_user_contact_method.get_user_contact,
            users_contacts_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_role_rights_method.get_role_rights,
            roles_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_role_method.get_role,
            roles_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_position_method.get_position,
            positions_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_department_method.get_department,
            departments_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_group_users_count_method.get_group_users_count,
            groups_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_group_users_ids_method.get_group_users_ids,
            groups_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_users_method.search_users,
            users_contacts_value,
            users_full_name,
            users_id,
            offices_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_upper_hierarchy_method.get_upper_hierarchy,
            users_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_users_departments_method.get_users_departments,
            users_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_users_groups_method.get_users_groups,
            users_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_positions_method.get_positions,
            users_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_group_method.get_group,
            groups_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_user_count_method.get_user_count,
            users_id,
            offices_id,
            users_contacts_value,
            users_full_name,
            count_of_request,
            duration,
            list_of_ammo,
            departments_id
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_user_contacts_method.search_user_contacts,
            users_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_user_settings_method.search_user_settings,
            users_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_ui_setting_method.search_ui_setting,
            users_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_roles_method.search_roles,
            users_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_positions_method.search_positions,
            users_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_office_users_method.get_office_users,
            offices_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_departments_method.search_departments,
            users_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_groups_method.search_groups,
            users_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_groups_count_method.get_groups_count,
            users_id,
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
