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
            database=dotenv_values(f"{currentdir}/.env_databases").get('clients_database')
        )
        connection_for_addresses_data = psycopg2.connect(
            user=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('user'),
            password=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('password'),
            host=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('host'),
            port=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('port'),
            database=dotenv_values(f"{currentdir}/.env_databases").get('addresses_database')
        )

        cursor = connection_for_addresses_data.cursor()

        print('Получаю cities_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"cities\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        cities_id = list(
            sum(
                result,
                ()
            )
        )

        cursor.close()

        cursor = connection.cursor()

        print('Получаю persons_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"persons\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        persons_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю realtors_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"realtors\" LIMIT 30000''')
        result = cursor.fetchall()
        realtors_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю agencies_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"agencies\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        agencies_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю contacts_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"contacts\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        contacts_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю contacts_value...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"contacts\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        contacts_value = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю contacts_type...')
        cursor.execute('''SELECT DISTINCT \"type\"
            from \"contacts\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        contacts_type = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю realtors_full_name...')
        cursor.execute('''SELECT DISTINCT \"fullName\"
            from \"realtors\" LIMIT 30000''')
        result = cursor.fetchall()
        realtors_full_name = list(
            sum(
                result,
                ()
            )
        )

        print("\nВсего получено записей:")
        print("persons_id: {0}".format(
            len(persons_id)
            )
        )
        print("realtors_id: {0}".format(
            len(realtors_id)
            )
        )
        print("cities_id: {0}".format(
            len(cities_id)
            )
        )
        print("agencies_id: {0}".format(
            len(agencies_id)
            )
        )
        print("contacts_id: {0}".format(
            len(contacts_id)
            )
        )
        print("contacts_value: {0}".format(
            len(contacts_value)
            )
        )
        print("contacts_type: {0}".format(
            len(contacts_type)
            )
        )
        print("realtors_full_name: {0}".format(
            len(realtors_full_name)
            )
        )

        result_info.append(
            persons_id
        )
        result_info.append(
            realtors_id
        )
        result_info.append(
            cities_id
        )
        result_info.append(
            agencies_id
        )
        result_info.append(
            contacts_id
        )
        result_info.append(
            contacts_value
        )
        result_info.append(
            contacts_type
        )
        result_info.append(
            realtors_full_name
        )

        return result_info

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
