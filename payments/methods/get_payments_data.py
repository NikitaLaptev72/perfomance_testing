import psycopg2
from psycopg2 import Error
from dotenv import dotenv_values


def get_info(
            target,
            currentdir
        ):
    result_info = []
    try:
        connection = psycopg2.connect(
            user=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('user'),
            password=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('password'),
            host=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('host'),
            port=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('port'),
            database=dotenv_values(f"{currentdir}/.env_databases").get('payments_database')
        )
        connection_for_user_data = psycopg2.connect(
            user=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('user'),
            password=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('password'),
            host=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('host'),
            port=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('port'),
            database=dotenv_values(f"{currentdir}/.env_databases").get('users_database')
        )

        cursor = connection_for_user_data.cursor()

        print('Получаю users_id...')
        cursor.execute('''SELECT DISTINCT \"users\".\"id\"
            from users where \"users\".\"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        users_id = list(
            sum(
                result,
                ()
            )
        )

        cursor.close()

        cursor = connection.cursor()

        print('Получаю bills_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"bills\" ''')
        result = cursor.fetchall()
        bills_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю bills_balance...')
        cursor.execute('''SELECT DISTINCT \"balance\"
            from \"bills\" ''')
        result = cursor.fetchall()
        bills_balance = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю bills_limit...')
        cursor.execute('''SELECT DISTINCT \"limit\"
            from \"bills\" ''')
        result = cursor.fetchall()
        bills_limit = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю bills_type...')
        cursor.execute('''SELECT DISTINCT \"type\"
            from \"bills\" ''')
        result = cursor.fetchall()
        bills_type = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю bills_status...')
        cursor.execute('''SELECT DISTINCT \"status\"
            from \"bills\" ''')
        result = cursor.fetchall()
        bills_status = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю payments_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"payments\" ''')
        result = cursor.fetchall()
        payments_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю payments_bill_from...')
        cursor.execute('''SELECT DISTINCT \"billFrom\"
            from \"payments\" ''')
        result = cursor.fetchall()
        payments_bill_from = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю payments_bill_to...')
        cursor.execute('''SELECT DISTINCT \"billTo\"
            from \"payments\" ''')
        result = cursor.fetchall()
        payments_bill_to = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю payments_amount...')
        cursor.execute('''SELECT DISTINCT \"amount\"
            from \"payments\" ''')
        result = cursor.fetchall()
        payments_amount = list(
            sum(
                result,
                ()
            )
        )

        print("\nВсего получено записей:")
        print("bills_id: {0}".format(
            len(bills_id)
            )
        )
        print("bills_balance: {0}".format(
            len(bills_balance)
            )
        )
        print("bills_limit: {0}".format(
            len(bills_limit)
            )
        )
        print("bills_type: {0}".format(
            len(bills_type)
            )
        )
        print("bills_status: {0}".format(
            len(bills_status)
            )
        )
        print("users_id: {0}".format(
            len(users_id)
            )
        )
        print("payments_id: {0}".format(
            len(payments_id)
            )
        )
        print("payments_bill_from: {0}".format(
            len(payments_bill_from)
            )
        )
        print("payments_bill_to: {0}".format(
            len(payments_bill_to)
            )
        )
        print("payments_amount: {0}".format(
            len(payments_amount)
            )
        )

        result_info.append(

            bills_id
        )
        result_info.append(
            bills_balance
        )
        result_info.append(
            bills_limit
        )
        result_info.append(
            bills_type
        )
        result_info.append(
            bills_status
        )
        result_info.append(
            users_id
        )
        result_info.append(
            payments_id
        )
        result_info.append(
            payments_bill_from
        )
        result_info.append(
            payments_bill_to
        )
        result_info.append(
            payments_amount
        )

        return result_info

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
