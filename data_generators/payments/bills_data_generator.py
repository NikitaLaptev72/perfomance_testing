from users.methods import get_users_data
import random as rnd
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


def bills_generator(target):
    bill_type = [
        1,
        2
    ]
    bill_status = [
        1,
        2
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

    connection.autocommit = True
    cursor = connection.cursor()
    for i in range(0, 100000):
        cursor.execute(
            '''INSERT INTO bills("userId", "type", "balance", "limit",
            "status") VALUES ({0}, {1}, {2}, {3}, {4})'''.format(
                rnd.choice(users_id),
                rnd.choice(bill_type),
                rnd.randint(100, 100000),
                1000000,
                rnd.choice(bill_status)
            )
        )

    connection.commit()
    connection.close()
