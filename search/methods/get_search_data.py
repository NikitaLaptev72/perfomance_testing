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
        connection_for_users = psycopg2.connect(
            user=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('user'),
            password=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('password'),
            host=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('host'),
            port=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('port'),
            database=dotenv_values(f"{currentdir}/.env_databases").get('users_database')
        )
        connection_for_tickets = psycopg2.connect(
            user=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('user'),
            password=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('password'),
            host=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('host'),
            port=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('port'),
            database=dotenv_values(f"{currentdir}/.env_databases").get('tickets_database')
        )
        connection_for_addresses = psycopg2.connect(
            user=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('user'),
            password=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('password'),
            host=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('host'),
            port=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('port'),
            database=dotenv_values(f"{currentdir}/.env_databases").get('addresses_database')
        )
        connection_for_clients = psycopg2.connect(
            user=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('user'),
            password=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('password'),
            host=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('host'),
            port=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('port'),
            database=dotenv_values(f"{currentdir}/.env_databases").get('clients_database')
        )
        connection_for_shows = psycopg2.connect(
            user=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('user'),
            password=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('password'),
            host=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('host'),
            port=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('port'),
            database=dotenv_values(f"{currentdir}/.env_databases").get('shows_database')
        )

        cursor = connection_for_shows.cursor()

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

        cursor.close()

        cursor = connection_for_clients.cursor()

        print('Получаю realtors_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"realtors\" ''')
        result = cursor.fetchall()
        realtors_id = list(
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

        cursor.close()

        cursor = connection_for_addresses.cursor()

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

        print('Получаю addresses_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"addressesData\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        addresses_id = list(
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

        cursor.close()

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

        print('Получаю tickets_alternative_stages...')
        cursor.execute('''SELECT DISTINCT \"alternativeStageId\"
            from tickets where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        tickets_alternative_stages = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю tickets_stages...')
        cursor.execute('''SELECT DISTINCT \"stageId\"
            from tickets where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        tickets_stages = list(
            sum(
                result,
                ()
            )
        )

        cursor.close()

        cursor = connection_for_users.cursor()

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

        print('Получаю offices_id...')
        cursor.execute('''SELECT DISTINCT \"usersOffices\".\"officeId\"
            from \"usersOffices\" where \"usersOffices\".\"officeId\" <> '0' ''')
        result = cursor.fetchall()
        offices_id = list(
            sum(
                result,
                ()
            )
        )

        cursor.close()

        cursor = connection_for_objects.cursor()

        print('Получаю general_plans_series...')
        cursor.execute('''SELECT DISTINCT \"series\"
            from \"generalPlans\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        general_plans_series = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю object_ids...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"objects\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        object_ids = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю class_object_ids...')
        cursor.execute('''SELECT DISTINCT \"class\"
            from \"objects\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        class_object_ids = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю type_object_ids...')
        cursor.execute('''SELECT DISTINCT \"type\"
            from \"objects\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        type_object_ids = list(
            sum(
                result,
                ()
            )
        )

        print("\nВсего получено записей:")
        print("general_plans_series: {0}".format(
            len(general_plans_series)
            )
        )
        print("users_id: {0}".format(
            len(users_id)
            )
        )
        print("offices_id: {0}".format(
            len(offices_id)
            )
        )
        print("tickets_id: {0}".format(
            len(tickets_id)
            )
        )
        print("tickets_alternative_stages: {0}".format(
            len(tickets_alternative_stages)
            )
        )
        print("tickets_stages: {0}".format(
            len(tickets_stages)
            )
        )
        print("cities_id: {0}".format(
            len(cities_id)
            )
        )
        print("realtors_id: {0}".format(
            len(realtors_id)
            )
        )
        print("addresses_id: {0}".format(
            len(addresses_id)
            )
        )
        print("shows_id: {0}".format(
            len(shows_id)
            )
        )
        print("object_ids: {0}".format(
            len(object_ids)
            )
        )
        print("regions_id: {0}".format(
            len(regions_id)
            )
        )
        print("streets_id: {0}".format(
            len(streets_id)
            )
        )
        print("areas_id: {0}".format(
            len(areas_id)
            )
        )
        print("areas_id: {0}".format(
            len(class_object_ids)
            )
        )
        print("areas_id: {0}".format(
            len(type_object_ids)
            )
        )

        result_info.append(
            general_plans_series
        )
        result_info.append(
            users_id
        )
        result_info.append(
            offices_id
        )
        result_info.append(
            tickets_id
        )
        result_info.append(
            tickets_alternative_stages
        )
        result_info.append(
            tickets_stages
        )
        result_info.append(
            cities_id
        )
        result_info.append(
            realtors_id
        )
        result_info.append(
            contacts_id
        )
        result_info.append(
            contacts_id
        )
        result_info.append(
            addresses_id
        )
        result_info.append(
            shows_id
        )
        result_info.append(
            object_ids
        )
        result_info.append(
            regions_id
        )
        result_info.append(
            streets_id
        )
        result_info.append(
            areas_id
        )
        result_info.append(
            class_object_ids
        )
        result_info.append(
            type_object_ids
        )

        return result_info

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection_for_objects):
            cursor.close()
            connection_for_objects.close()
