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
            database=dotenv_values(f"{currentdir}/.env_databases").get('users_database')
        )

        cursor = connection.cursor()

        print('Получаю users_full_name...')
        cursor.execute('''SELECT DISTINCT \"users\".\"fullName\"
            from users where \"users\".\"deletedAt\" IS NULL
                and \"users\".\"fullName\" <> '' ''')
        result = cursor.fetchall()
        users_full_name = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю users_contacts_value...')
        cursor.execute('''SELECT DISTINCT \"contacts\".\"value\"
            from contacts where \"contacts\".\"deletedAt\" IS NULL
                and \"contacts\".\"value\" <> '' ''')
        result = cursor.fetchall()
        users_contacts = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю users_contacts_id...')
        cursor.execute('''SELECT DISTINCT \"contacts\".\"id\"
            from contacts where \"contacts\".\"deletedAt\" IS NULL
                and \"contacts\".\"value\" <> '' ''')
        result = cursor.fetchall()
        users_contacts_id = list(
            sum(
                result,
                ()
            )
        )

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

        print('Получаю roles_id...')
        cursor.execute('''SELECT DISTINCT \"roles\".\"id\" from roles''')
        result = cursor.fetchall()
        roles_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю positions_id...')
        cursor.execute('''SELECT DISTINCT \"positions\".\"id\" from positions''')
        result = cursor.fetchall()
        positions_id = list(
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

        print('Получаю departments_id...')
        cursor.execute('''SELECT DISTINCT \"departments\".\"id\"
            from departments where \"departments\".\"name\" <> '' ''')
        result = cursor.fetchall()
        departments_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю groups_id...')
        cursor.execute('''SELECT DISTINCT \"groups\".\"id\" from groups''')
        result = cursor.fetchall()
        groups_id = list(
            sum(
                result,
                ()
            )
        )

        print("\nВсего получено записей:")
        print("users_full_name: {0}".format(
            len(users_full_name)
            )
        )
        print("users_contacts: {0}".format(
            len(users_contacts)
            )
        )
        print("users_contacts_id: {0}".format(
            len(users_contacts_id)
            )
        )
        print("users_id: {0}".format(
            len(users_id)
            )
        )
        print("roles_id: {0}".format(
            len(roles_id)
            )
        )
        print("positions_id: {0}".format(
            len(positions_id)
            )
        )
        print("offices_id: {0}".format(
            len(offices_id)
            )
        )
        print("groups_id: {0}".format(
            len(groups_id)
            )
        )

        result_info.append(
            users_full_name
        )
        result_info.append(
            users_contacts
        )
        result_info.append(
            users_contacts_id
        )
        result_info.append(
            users_id
        )
        result_info.append(
            roles_id
        )
        result_info.append(
            positions_id
        )
        result_info.append(
            offices_id
        )
        result_info.append(
            departments_id
        )
        result_info.append(
            groups_id
        )

        return result_info

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
