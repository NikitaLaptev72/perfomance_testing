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
            database=dotenv_values(f"{currentdir}/.env_databases").get('tasks_database')
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
        users_offices_ids = list(
            sum(
                result,
                ()
            )
        )

        cursor.close()

        cursor = connection.cursor()

        print('Получаю tasks_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from tasks where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        tasks_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю templates_Id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from templates where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        templates_Id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю temp_tasks_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"tempTasks\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        temp_tasks_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю entities_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"entities\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        entities_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю created_at_task...')
        cursor.execute('''SELECT DISTINCT \"createdAt\"
            from \"tasks\" ''')
        result = cursor.fetchall()
        created_at_task = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю description_task...')
        cursor.execute('''SELECT DISTINCT \"description\"
            from \"tasks\" where \"description\" IS NOT NULL''')
        result = cursor.fetchall()
        description_task = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю memberIds...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"members\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        memberIds = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю sub_statuses_names...')
        cursor.execute('''SELECT DISTINCT \"name\" from \"substatuses\" ''')
        result = cursor.fetchall()
        sub_statuses_names = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю OfficesId...')
        cursor.execute('''SELECT DISTINCT \"officeId\"
            from \"substatuses\" where \"officeId\" <> '0' ''')
        result = cursor.fetchall()
        offices_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю checklists_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"checklists\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        checklists_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю creators_ids...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"checklists\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        creators_ids = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю field_id...')
        cursor.execute('''SELECT DISTINCT \"fieldId\"
            from \"fieldsValues\" ''')
        result = cursor.fetchall()
        field_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю task_titles...')
        cursor.execute('''SELECT DISTINCT \"title\"
            from \"tasks\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        task_titles = list(
            sum(
                result,
                ()
            )
        )

        print("\nВсего получено записей:")
        print("tasks_id: {0}".format(
            len(tasks_id)
            )
        )
        print("templates_Id: {0}".format(
            len(templates_Id)
            )
        )
        print("TempTask_Id: {0}".format(
            len(temp_tasks_id)
            )
        )
        print("entities_id: {0}".format(
            len(entities_id)
            )
        )
        print("created_at_task: {0}".format(
            len(created_at_task)
            )
        )
        print("description_task: {0}".format(
            len(description_task)
            )
        )
        print("memberIds: {0}".format(
            len(memberIds)
            )
        )
        print("sub_statuses_names: {0}".format(
            len(sub_statuses_names)
            )
        )
        print("offices_id: {0}".format(
            len(offices_id)
            )
        )
        print("users_offices_ids: {0}".format(
            len(users_offices_ids)
            )
        )
        print("checklists_id: {0}".format(
            len(checklists_id)
            )
        )
        print("creators_ids: {0}".format(
            len(creators_ids)
            )
        )
        print("field_id: {0}".format(
            len(field_id)
            )
        )
        print("task_titles: {0}".format(
            len(task_titles)
            )
        )

        result_info.append(
            tasks_id
        )
        result_info.append(
            templates_Id
        )
        result_info.append(
            temp_tasks_id
        )
        result_info.append(
            entities_id
        )
        result_info.append(
            created_at_task
        )
        result_info.append(
            description_task
        )
        result_info.append(
            memberIds
        )
        result_info.append(
            sub_statuses_names
        )
        result_info.append(
            offices_id
        )
        result_info.append(
            users_offices_ids
        )
        result_info.append(
            checklists_id
        )
        result_info.append(
            creators_ids
        )
        result_info.append(
            field_id
        )
        result_info.append(
            task_titles
        )

        return result_info

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
