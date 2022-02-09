from shows.methods import get_shows_data
from shows.methods.with_body import get_shows_method
from shows.methods.with_body import get_count_shows_method
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
    incoming_shows_info = get_shows_data.get_info(
        target,
        currentdir
    )
    tickets_id = incoming_shows_info[0]
    shows_id = incoming_shows_info[1]
    status_shows_id = incoming_shows_info[2]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            get_shows_method.get_shows,
            tickets_id,
            shows_id,
            status_shows_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_count_shows_method.get_count_shows,
            tickets_id,
            shows_id,
            status_shows_id,
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
