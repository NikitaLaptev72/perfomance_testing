from users.methods import get_users_data
from payments.methods import get_payments_data
import random as rnd
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


def payments_generator(target):
    paymentStatus = [
        1,
        2,
        3
    ]
    connection = psycopg2.connect(
        user=os.getenv(f'user_{target.lower()}'),
        password=os.getenv(f'password_{target.lower()}'),
        host=os.getenv(f'host_{target.lower()}'),
        port=os.getenv(f'port_{target.lower()}'),
        database=os.getenv(f'payments_database_{target.lower()}')
    )

    incoming_users_info = get_users_data.get_info(target)
    users_id = incoming_users_info[3]
    IncomingPaymentsInfo = get_payments_data.get_info(target)
    bills_id = IncomingPaymentsInfo[0]

    connection.autocommit = True
    cursor = connection.cursor()
    for i in range(0, 100000):
        bills_from = rnd.choice(bills_id)
        bills_to = rnd.choice(bills_id)
        if bills_from == bills_to:
            while bills_from == bills_to:
                bills_from = rnd.choice(bills_id)
                bills_to = rnd.choice(bills_id)
        cursor.execute(
            '''INSERT INTO payments("billFrom", "billTo", "amount", "operatorId",
            "categoryId", "status", "comment") VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6})'''.format(
                bills_from,
                bills_to,
                rnd.randint(0, 8),
                rnd.choice(users_id),
                rnd.randint(1, 2),
                rnd.choice(paymentStatus),
                rnd.randint(1, 1000)
            )
        )
    connection.commit()
    connection.close()
