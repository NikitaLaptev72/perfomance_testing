from attachments.methods import get_attchments_data
from attachments.methods.with_body import get_attachments_method
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
    incoming_attachments_info = get_attchments_data.get_info(
        target,
        currentdir
    )
    attachments_id = incoming_attachments_info[0]
    attachments_name = incoming_attachments_info[1]
    relations_entity = incoming_attachments_info[2]
    relations_entity_id = incoming_attachments_info[3]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            get_attachments_method.get_attachments,
            attachments_id,
            attachments_name,
            relations_entity,
            relations_entity_id,
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
