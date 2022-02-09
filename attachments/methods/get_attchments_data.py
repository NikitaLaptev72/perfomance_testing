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
            database=dotenv_values(f"{currentdir}/.env_databases").get('attachments_database')
        )

        cursor = connection.cursor()

        print('Получаю attachments_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"attachments\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        attachments_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю attachments_name...')
        cursor.execute('''SELECT DISTINCT \"name\"
            from \"attachments\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        attachments_name = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю relations_entity...')
        cursor.execute('''SELECT DISTINCT \"entity\"
            from \"relations\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        relations_entity = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю relations_entity_id...')
        cursor.execute('''SELECT DISTINCT \"entityId\"
            from \"relations\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        relations_entity_id = list(
            sum(
                result,
                ()
            )
        )

        print("\nВсего получено записей:")
        print("attachments_id: {0}".format(
            len(attachments_id)
            )
        )
        print("attachments_name: {0}".format(
            len(attachments_name)
            )
        )
        print("relations_entity: {0}".format(
            len(relations_entity)
            )
        )
        print("relations_entity_id: {0}".format(
            len(relations_entity_id)
            )
        )

        result_info.append(
            attachments_id
            )
        result_info.append(
            attachments_name
            )
        result_info.append(
            relations_entity
            )
        result_info.append(
            relations_entity_id
            )

        return result_info

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
