import psycopg2
from psycopg2 import Error
from dotenv import dotenv_values


def get_info(
            target,
            currentdir
        ):
    result_info = []
    try:
        connection_for_objects = psycopg2.connect(
            user=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('user'),
            password=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('password'),
            host=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('host'),
            port=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('port'),
            database=dotenv_values(f"{currentdir}/.env_databases").get('objects_database')
        )
        connection = psycopg2.connect(
            user=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('user'),
            password=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('password'),
            host=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('host'),
            port=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('port'),
            database=dotenv_values(f"{currentdir}/.env_databases").get('attachments_database')
        )

        cursor = connection_for_objects.cursor()

        print('Получаю objects_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"objects\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        objects_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю general_plans_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"generalPlans\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        general_plans_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю housing_complexes_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"housingComplexes\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        housing_complexes_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю series_general_plans...')
        cursor.execute('''SELECT DISTINCT \"series\"
            from \"generalPlans\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        series_general_plans = list(
            sum(
                result,
                ()
            )
        )

        cursor.close()

        cursor = connection.cursor()

        print('Получаю entity_id...')
        cursor.execute('''SELECT DISTINCT \"entityId\"
            from \"relations\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        entity_id = list(
            sum(
                result,
                ()
            )
        )

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

        print("\nВсего получено записей:")
        print("objects_id: {0}".format(
            len(objects_id)
            )
        )
        print("general_plans_id: {0}".format(
            len(general_plans_id)
            )
        )
        print("housing_complexes_id: {0}".format(
            len(housing_complexes_id)
            )
        )
        print("entity_id: {0}".format(
            len(entity_id)
            )
        )
        print("attachments_id: {0}".format(
            len(attachments_id)
            )
        )
        print("series_general_plans: {0}".format(
            len(series_general_plans)
            )
        )

        result_info.append(
            objects_id
        )
        result_info.append(
            general_plans_id
        )
        result_info.append(
            housing_complexes_id
        )
        result_info.append(
            entity_id
        )
        result_info.append(
            attachments_id
        )
        result_info.append(
            series_general_plans
        )

        return result_info

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
        if (connection_for_objects):
            cursor.close()
            connection_for_objects.close()
