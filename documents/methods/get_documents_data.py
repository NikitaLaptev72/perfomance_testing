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
            database=dotenv_values(f"{currentdir}/.env_databases").get('documents_database')
        )
        connection_for_users_data = psycopg2.connect(
            user=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('user'),
            password=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('password'),
            host=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('host'),
            port=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('port'),
            database=dotenv_values(f"{currentdir}/.env_databases").get('users_database')
        )

        cursor = connection_for_users_data.cursor()

        print('Получаю users_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"users\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        users_id = list(
            sum(
                result,
                ()
            )
        )

        cursor.close()

        cursor = connection.cursor()

        print('Получаю documents_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"documents\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        documents_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю documentstype_id...')
        cursor.execute('''SELECT DISTINCT \"typeId\"
            from \"documents\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        documentstype_id = list(
            sum(
                result,
                ()
            )
        )

        print("\nВсего получено записей:")
        print("documents_id: {0}".format(
            len(documents_id)
            )
        )
        print("users_id: {0}".format(
            len(users_id)
            )
        )
        print("documentstype_id: {0}".format(
            len(documentstype_id)
            )
        )

        result_info.append(
            documents_id
        )
        result_info.append(
            users_id
        )
        result_info.append(
            documentstype_id
        )

        return result_info

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
