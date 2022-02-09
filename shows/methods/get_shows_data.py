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
            database=dotenv_values(f"{currentdir}/.env_databases").get('shows_database')
        )
        connection_for_tickets = psycopg2.connect(
            user=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('user'),
            password=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('password'),
            host=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('host'),
            port=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('port'),
            database=dotenv_values(f"{currentdir}/.env_databases").get('tickets_database')
        )

        cursor = connection_for_tickets.cursor()

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

        cursor.close()

        cursor = connection.cursor()

        print('Получаю shows_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from shows where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        shows_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю status_shows_id...')
        cursor.execute('''SELECT DISTINCT \"status\"
            from shows where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        status_shows_id = list(
            sum(
                result,
                ()
            )
        )

        cursor.close()

        print("\nВсего получено записей:")
        print("tickets_id: {0}".format(
                len(tickets_id)
            )
        )
        print("shows_id: {0}".format(
            len(shows_id)
            )
        )
        print("status_shows_id: {0}".format(
            len(status_shows_id)
            )
        )

        result_info.append(
            tickets_id
        )
        result_info.append(
            shows_id
        )
        result_info.append(
            status_shows_id)

        return result_info

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
