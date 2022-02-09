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
            database=dotenv_values(f"{currentdir}/.env_databases").get('addresses_database')
        )

        cursor = connection.cursor()

        print('Получаю adresses_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"addressesData\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        adresses_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю adresses_value...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"addressesData\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        adresses_value = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю country_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"countries\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        country_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю federal_districts_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"federalDistricts\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        federal_districts_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю regions_id...')
        cursor.execute('''SELECT DISTINCT \"id\" from
            \"regions\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        regions_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю areas_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"areas\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        areas_id = list(
            sum(
                result,
                ()
            )
        )

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

        print('Получаю settlements_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"settlements\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        settlements_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю districts_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"districts\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        districts_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю streets_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"streets\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        streets_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю city_name...')
        cursor.execute('''SELECT DISTINCT \"cityName\"
            from \"cities\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        city_name = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю patch_id...')
        cursor.execute('''SELECT DISTINCT \"patchId\"
            from \"customComponentsPatches\" LIMIT 30000''')
        result = cursor.fetchall()
        patch_id = list(
            sum(
                result,
                ()
            )
        )

        print("\nВсего получено записей:")
        print("adresses_id: {0}".format(
            len(adresses_id)
            )
        )
        print("adresses_value: {0}".format(
            len(adresses_value)
            )
        )
        print("country_id: {0}".format(
            len(country_id)
            )
        )
        print("federal_districts_id: {0}".format(
            len(federal_districts_id)
            )
        )
        print("regions_id: {0}".format(
            len(regions_id)
            )
        )
        print("areas_id: {0}".format(
            len(areas_id)
            )
        )
        print("cities_id: {0}".format(
            len(cities_id)
            )
        )
        print("settlements_id: {0}".format(
            len(settlements_id)
            )
        )
        print("districts_id: {0}".format(
            len(districts_id)
            )
        )
        print("streets_id: {0}".format(
            len(streets_id)
            )
        )
        print("city_name: {0}".format(
            len(city_name)
            )
        )
        print("patch_id: {0}".format(
            len(patch_id)
            )
        )

        result_info.append(
            adresses_id
        )
        result_info.append(
            adresses_value
        )
        result_info.append(
            country_id
        )
        result_info.append(
            federal_districts_id
        )
        result_info.append(
            regions_id
        )
        result_info.append(
            areas_id
        )
        result_info.append(
            cities_id
        )
        result_info.append(
            settlements_id
        )
        result_info.append(
            districts_id
        )
        result_info.append(
            streets_id
        )
        result_info.append(
            city_name
        )
        result_info.append(
            patch_id
        )

        return result_info

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
