from tasks.methods import get_tasks_data
from tasks.methods.with_parameters import get_task_method
from tasks.methods.with_parameters import get_template_method
from tasks.methods.with_parameters import get_chain_method
from tasks.methods.with_parameters import get_check_list_method
from tasks.methods.with_parameters import get_childs_ids_method
from tasks.methods.with_parameters import get_childs_method
from tasks.methods.with_parameters import get_parent_task_method
from tasks.methods.with_parameters import get_temp_parent_task_method
from tasks.methods.with_parameters import get_temp_task_method
from tasks.methods.with_body import search_entities_method
from tasks.methods.with_body import search_tasks_to_set_as_parent_method
from tasks.methods.with_body import search_temp_entities_method
from tasks.methods.with_body import get_count_tasks_method
from tasks.methods.with_body import get_entities_count_method
from tasks.methods.with_body import get_members_method
from tasks.methods.with_body import get_substatuses_categories_method
from tasks.methods.with_body import get_substatuses_method
from tasks.methods.with_body import search_check_items_method
from tasks.methods.with_body import get_templates_count_method
from tasks.methods.with_body import search_templates_method
from tasks.methods.with_body import search_tasks_method
from tasks.methods.with_body_and_parameters import get_fields_values_method
from tasks.methods.with_body_and_parameters import get_temp_fields_values_method
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
    incoming_tasks_info = get_tasks_data.get_info(
        target,
        currentdir
    )
    tasks_id = incoming_tasks_info[0]
    templates_Id = incoming_tasks_info[1]
    temp_tasks_id = incoming_tasks_info[2]
    entities_id = incoming_tasks_info[3]
    created_at_task = incoming_tasks_info[4]
    description_task = incoming_tasks_info[5]
    members_ids = incoming_tasks_info[6]
    sub_statuses_names = incoming_tasks_info[7]
    offices_id = incoming_tasks_info[8]
    users_offices_ids = incoming_tasks_info[9]
    checklists_id = incoming_tasks_info[10]
    сreators_ids = incoming_tasks_info[11]
    field_id = incoming_tasks_info[12]
    task_titles = incoming_tasks_info[13]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            get_task_method.get_task,
            tasks_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_template_method.get_template,
            templates_Id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_chain_method.get_chain,
            templates_Id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_check_list_method.get_check_list,
            tasks_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_childs_ids_method.get_childs_ids,
            tasks_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_childs_method.get_childs,
            tasks_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_parent_task_method.get_parent_task,
            tasks_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_temp_parent_task_method.get_temp_parent_task,
            temp_tasks_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_temp_task_method.get_temp_task,
            temp_tasks_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_entities_method.search_entities,
            tasks_id,
            entities_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_tasks_to_set_as_parent_method.search_tasks_to_set_as_parent,
            tasks_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_temp_entities_method.search_temp_entities,
            tasks_id,
            entities_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_count_tasks_method.get_count_tasks,
            tasks_id,
            created_at_task,
            description_task,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_entities_count_method.get_entities_count,
            entities_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_members_method.get_members,
            members_ids,
            tasks_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_substatuses_categories_method.get_substatuses_categories,
            sub_statuses_names,
            offices_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_substatuses_method.get_substatuses,
            sub_statuses_names,
            offices_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_check_items_method.search_check_items,
            checklists_id,
            tasks_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_templates_count_method.get_templates_count,
            templates_Id,
            users_offices_ids,
            сreators_ids,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_templates_method.search_templates,
            templates_Id,
            users_offices_ids,
            сreators_ids,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_fields_values_method.get_fields_values,
            tasks_id,
            field_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_temp_fields_values_method.get_temp_fields_values,
            temp_tasks_id,
            field_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_tasks_method.search_tasks,
            task_titles,
            tasks_id,
            description_task,
            users_offices_ids,
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
