from documents.methods import get_documents_data
from documents.methods.with_body import count_documents_method
from documents.methods.with_body import search_documents_method
from documents.methods.with_body import search_fields_method
from documents.methods.with_body_and_parameters import get_document_method
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
    IncomingDocumentsInfo = get_documents_data.get_info(
        target,
        currentdir
    )
    documents_id = IncomingDocumentsInfo[0]
    users_id = IncomingDocumentsInfo[1]
    documents_type_id = IncomingDocumentsInfo[2]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            count_documents_method.count_documents,
            documents_id,
            users_id,
            documents_type_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_documents_method.search_documents,
            documents_id,
            users_id,
            documents_type_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_fields_method.search_fields,
            documents_id,
            documents_type_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_document_method.get_document,
            documents_id,
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
