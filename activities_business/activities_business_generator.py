from activities_business.methods import get_activities_business_data
from activities_business.methods.with_body import search_activities_method
from activities_business.methods.with_body import search_calendar_activities_method
from activities_business.methods.with_body import search_meetings_method
from activities_business.methods.with_body import get_meetings_count_method
from activities_business.methods.with_body import get_activities_count_method
from activities_business.methods.with_parameters import get_activity_method
from activities_business.methods.with_parameters import get_activity_permissions_method
from activities_business.methods.with_parameters import get_confirm_method
from activities_business.methods.with_body_and_parameters import get_activity_fields_method
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
    incoming_activities_info = get_activities_business_data.get_info(
        target,
        currentdir
    )
    activities_id = incoming_activities_info[0]
    type_id_activities_id = incoming_activities_info[1]
    status_id_activities_id = incoming_activities_info[2]
    description_activities_id = incoming_activities_info[3]
    start_dateactivities_id = incoming_activities_info[4]
    end_date_activities_id = incoming_activities_info[5]
    speaker_activities_fields = incoming_activities_info[6]
    city_activities_fields = incoming_activities_info[7]
    for_whom_activities_fields = incoming_activities_info[8]
    format_activities_fields = incoming_activities_info[9]
    scale_activities_fields = incoming_activities_info[10]
    name_activities_fields = incoming_activities_info[11]
    price_activities_fields = incoming_activities_info[12]
    where_activities_fields = incoming_activities_info[13]
    translation_link_activities_fields = incoming_activities_info[14]
    for_which_city_activities_fields = incoming_activities_info[15]
    notification_activities_fields = incoming_activities_info[16]
    result_activities_fields = incoming_activities_info[17]
    comment_activities_fields = incoming_activities_info[18]
    topic_activities_fields = incoming_activities_info[19]
    office_activities_fields = incoming_activities_info[20]
    entity_id = incoming_activities_info[21]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            search_activities_method.search_activities,
            activities_id,
            type_id_activities_id,
            status_id_activities_id,
            description_activities_id,
            start_dateactivities_id,
            end_date_activities_id,
            speaker_activities_fields,
            city_activities_fields,
            for_whom_activities_fields,
            format_activities_fields,
            scale_activities_fields,
            name_activities_fields,
            price_activities_fields,
            where_activities_fields,
            translation_link_activities_fields,
            for_which_city_activities_fields,
            notification_activities_fields,
            result_activities_fields,
            comment_activities_fields,
            topic_activities_fields,
            office_activities_fields,
            entity_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_calendar_activities_method.search_calendar_activities,
            activities_id,
            type_id_activities_id,
            status_id_activities_id,
            description_activities_id,
            start_dateactivities_id,
            end_date_activities_id,
            speaker_activities_fields,
            city_activities_fields,
            for_whom_activities_fields,
            format_activities_fields,
            scale_activities_fields,
            name_activities_fields,
            price_activities_fields,
            where_activities_fields,
            translation_link_activities_fields,
            for_which_city_activities_fields,
            notification_activities_fields,
            result_activities_fields,
            comment_activities_fields,
            topic_activities_fields,
            office_activities_fields,
            entity_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_activities_count_method.get_activities_count,
            activities_id,
            type_id_activities_id,
            status_id_activities_id,
            description_activities_id,
            start_dateactivities_id,
            end_date_activities_id,
            speaker_activities_fields,
            city_activities_fields,
            for_whom_activities_fields,
            format_activities_fields,
            scale_activities_fields,
            name_activities_fields,
            price_activities_fields,
            where_activities_fields,
            translation_link_activities_fields,
            for_which_city_activities_fields,
            notification_activities_fields,
            result_activities_fields,
            comment_activities_fields,
            topic_activities_fields,
            office_activities_fields,
            entity_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            search_meetings_method.search_meetings,
            activities_id,
            type_id_activities_id,
            status_id_activities_id,
            description_activities_id,
            start_dateactivities_id,
            end_date_activities_id,
            speaker_activities_fields,
            city_activities_fields,
            for_whom_activities_fields,
            format_activities_fields,
            scale_activities_fields,
            name_activities_fields,
            price_activities_fields,
            where_activities_fields,
            translation_link_activities_fields,
            for_which_city_activities_fields,
            notification_activities_fields,
            result_activities_fields,
            comment_activities_fields,
            topic_activities_fields,
            office_activities_fields,
            entity_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_meetings_count_method.get_meetings_count,
            activities_id,
            type_id_activities_id,
            status_id_activities_id,
            description_activities_id,
            start_dateactivities_id,
            end_date_activities_id,
            speaker_activities_fields,
            city_activities_fields,
            for_whom_activities_fields,
            format_activities_fields,
            scale_activities_fields,
            name_activities_fields,
            price_activities_fields,
            where_activities_fields,
            translation_link_activities_fields,
            for_which_city_activities_fields,
            notification_activities_fields,
            result_activities_fields,
            comment_activities_fields,
            topic_activities_fields,
            office_activities_fields,
            entity_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_activity_permissions_method.get_activity_permissions,
            activities_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_activity_method.get_activity,
            activities_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_confirm_method.get_confirm,
            activities_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_activity_fields_method.get_activity_fields_values,
            activities_id,
            start_dateactivities_id,
            end_date_activities_id,
            type_id_activities_id,
            speaker_activities_fields,
            city_activities_fields,
            format_activities_fields,
            name_activities_fields,
            description_activities_id,
            price_activities_fields,
            translation_link_activities_fields,
            result_activities_fields,
            comment_activities_fields,
            topic_activities_fields,
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
