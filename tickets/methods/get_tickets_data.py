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
            database=dotenv_values(f"{currentdir}/.env_databases").get('tickets_database')
        )
        connection_for_clients = psycopg2.connect(
            user=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('user'),
            password=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('password'),
            host=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('host'),
            port=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('port'),
            database=dotenv_values(f"{currentdir}/.env_databases").get('clients_database')
        )
        connection_for_users_data = psycopg2.connect(
            user=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('user'),
            password=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('password'),
            host=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('host'),
            port=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('port'),
            database=dotenv_values(f"{currentdir}/.env_databases").get('users_database')
        )

        cursor = connection_for_users_data.cursor()

        print('Получаю offices_id...')
        cursor.execute('''SELECT DISTINCT \"usersOffices\".\"officeId\"
            from \"usersOffices\" where \"usersOffices\".\"officeId\" <> '0' ''')
        result = cursor.fetchall()
        offices_ids = list(
            sum(
                result,
                ()
            )
        )

        cursor.close()

        cursor = connection_for_clients.cursor()

        print('Получаю clients_id...')
        cursor.execute('''SELECT DISTINCT \"clientId\"
            from contacts where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        clients_id = list(
            sum(
                result,
                ()
            )
        )

        cursor.close()
        cursor = connection.cursor()

        print('Получаю tickets_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from tickets where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        tickets_id = list(
            sum(
                result,
                ()
            )
        )

        print("\nВсего получено записей:")
        print("tickets_id: {0}" .format(
            len(tickets_id)
            )
        )
        print("clients_id: {0}" .format(
            len(clients_id)
            )
        )
        print("offices_ids: {0}" .format(
            len(offices_ids)
            )
        )

        result_info.append(
            tickets_id
        )
        result_info.append(
            clients_id
        )
        result_info.append(offices_ids)

        return result_info

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
