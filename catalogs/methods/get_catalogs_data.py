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
            database=dotenv_values(f"{currentdir}/.env_databases").get('catalogs_database')
        )

        cursor = connection.cursor()

        print('Получаю catalogs_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"catalogs\" where \"deleted_at\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        catalogs_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю catalogs_name...')
        cursor.execute('''SELECT DISTINCT \"name\"
            from \"catalogs\" where \"deleted_at\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        catalogs_name = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю catalogs_title...')
        cursor.execute('''SELECT DISTINCT \"title\"
            from \"catalogs\" where \"deleted_at\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        catalogs_title = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю catalogs_description...')
        cursor.execute('''SELECT DISTINCT \"description\"
            from \"catalogs\" where \"deleted_at\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        catalogs_description = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю uuid_catalog_items...')
        cursor.execute('''SELECT DISTINCT \"uuid\"
            from \"catalog_items\" where \"deleted_at\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        uuid_catalog_items = list(
            sum(
                result,
                ()
            )
        )

        print("\nВсего получено записей:")
        print("catalogs_id: {0}".format(
            len(catalogs_id)
            )
        )
        print("catalogs_name: {0}".format(
            len(catalogs_name)
            )
        )
        print("catalogs_title: {0}".format(
            len(catalogs_title)
            )
        )
        print("catalogs_description: {0}".format(
            len(catalogs_description)
            )
        )
        print("uuid_catalog_items: {0}".format(
            len(uuid_catalog_items)
            )
        )

        result_info.append(
            catalogs_id
        )
        result_info.append(
            catalogs_name
        )
        result_info.append(
            catalogs_title
        )
        result_info.append(
            catalogs_description
        )
        result_info.append(
            uuid_catalog_items
        )

        return result_info

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
