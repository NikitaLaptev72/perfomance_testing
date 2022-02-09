from payments.methods import get_payments_data
from payments.methods.with_body import get_bills_method
from payments.methods.with_body import get_payments_method
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
    incoming_payments_info = get_payments_data.get_info(
        target,
        currentdir
    )
    bills_id = incoming_payments_info[0]
    bills_balance = incoming_payments_info[1]
    bills_limit = incoming_payments_info[2]
    bills_type = incoming_payments_info[3]
    bills_status = incoming_payments_info[4]
    users_id = incoming_payments_info[5]
    payments_id = incoming_payments_info[6]
    payments_bill_from = incoming_payments_info[7]
    paymentsbill_to = incoming_payments_info[8]
    payments_amount = incoming_payments_info[9]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            get_bills_method.get_bills,
            bills_id,
            bills_balance,
            bills_limit,
            bills_type,
            bills_status,
            users_id,
            count_of_request,
            duration,
            list_of_ammo
        )
        count_of_request, list_of_ammo = future.result()

        future = executor.submit(
            get_payments_method.get_payments,
            payments_id,
            bills_id,
            payments_bill_from,
            paymentsbill_to,
            payments_amount,
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
