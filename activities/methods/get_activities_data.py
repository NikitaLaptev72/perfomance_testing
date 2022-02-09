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
            database=dotenv_values(f"{currentdir}/.env_databases").get('activities_database')
        )
        cursor = connection.cursor()

        print('Получаю activities_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"activities\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        activities_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю type_id_activities_id...')
        cursor.execute('''SELECT DISTINCT \"typeId\"
            from \"activities\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        type_id_activities_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю status_id_activities_id...')
        cursor.execute('''SELECT DISTINCT \"statusId\"
            from \"activities\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        status_id_activities_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю description_activities_id...')
        cursor.execute('''SELECT DISTINCT \"description\"
            from \"activities\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        description_activities_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю start_date_activities_id...')
        cursor.execute('''SELECT DISTINCT \"startDate\"
            from \"activities\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        start_date_activities_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю end_date_activities_id...')
        cursor.execute('''SELECT DISTINCT \"endDate\"
            from \"activities\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        end_date_activities_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю speaker_activities_fields...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"activitiesFields\" where \"name\" = 'speaker' ''')
        result = cursor.fetchall()
        speaker_activities_fields = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю city_activities_fields...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"activitiesFields\" where \"name\" = 'city' ''')
        result = cursor.fetchall()
        city_activities_fields = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю for_whom_activities_fields...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"activitiesFields\" where \"name\" = 'forWhom' ''')
        result = cursor.fetchall()
        for_whom_activities_fields = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю format_activities_fields...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"activitiesFields\" where \"name\" = 'format' ''')
        result = cursor.fetchall()
        format_activities_fields = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю scale_activities_fields...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"activitiesFields\" where \"name\" = 'scale' ''')
        result = cursor.fetchall()
        scale_activities_fields = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю name_activities_fields...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"activitiesFields\" where \"name\" = 'name' ''')
        result = cursor.fetchall()
        name_activities_fields = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю price_activities_fields...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"activitiesFields\" where \"name\" = 'price' ''')
        result = cursor.fetchall()
        price_activities_fields = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю where_activities_fields...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"activitiesFields\" where \"name\" = 'where' ''')
        result = cursor.fetchall()
        where_activities_fields = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю translation_link_activities_fields...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"activitiesFields\" where \"name\" = 'translationLink' ''')
        result = cursor.fetchall()
        translation_link_activities_fields = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю for_which_city_activities_fields...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"activitiesFields\" where \"name\" = 'forWhichCity' ''')
        result = cursor.fetchall()
        for_which_city_activities_fields = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю notification_activities_fields...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"activitiesFields\" where \"name\" = 'notification' ''')
        result = cursor.fetchall()
        notification_activities_fields = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю result_activities_fields...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"activitiesFields\" where \"name\" = 'result' ''')
        result = cursor.fetchall()
        result_activities_fields = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю comment_activities_fields...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"activitiesFields\" where \"name\" = 'comment' ''')
        result = cursor.fetchall()
        comment_activities_fields = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю topic_activities_fields...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"activitiesFields\" where \"name\" = 'topic' ''')
        result = cursor.fetchall()
        topic_activities_fields = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю office_activities_fields...')
        cursor.execute('''SELECT DISTINCT \"value\"
            from \"activitiesFields\" where \"name\" = 'office' ''')
        result = cursor.fetchall()
        office_activities_fields = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю entity_id...')
        cursor.execute('''SELECT DISTINCT \"entityId\"
            from \"entities\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        entity_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю entity...')
        cursor.execute('''SELECT DISTINCT \"entity\"
            from \"entities\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        entity = list(
            sum(
                result,
                ()
            )
        )

        print("\nВсего получено записей:")
        print("activities_id: {0}".format(
            len(activities_id)
            )
        )
        print("type_id_activities_id: {0}".format(
            len(type_id_activities_id)
            )
        )
        print("status_id_activities_id: {0}".format(
            len(status_id_activities_id)
            )
        )
        print("description_activities_id: {0}".format(
            len(description_activities_id)
            )
        )
        print("start_date_activities_id: {0}".format(
            len(start_date_activities_id)
            )
        )
        print("end_date_activities_id: {0}".format(
            len(end_date_activities_id)
            )
        )
        print("speaker_activities_fields: {0}".format(
            len(speaker_activities_fields)
            )
        )
        print("city_activities_fields: {0}".format(
            len(city_activities_fields)
            )
        )
        print("for_whom_activities_fields: {0}".format(
            len(for_whom_activities_fields)
            )
        )
        print("format_activities_fields: {0}".format(
            len(format_activities_fields)
            )
        )
        print("scale_activities_fields: {0}".format(
            len(scale_activities_fields)
            )
        )
        print("name_activities_fields: {0}".format(
            len(name_activities_fields)
            )
        )
        print("price_activities_fields: {0}".format(
            len(price_activities_fields)
            )
        )
        print("where_activities_fields: {0}".format(
            len(where_activities_fields)
            )
        )
        print("translation_link_activities_fields: {0}".format(
            len(translation_link_activities_fields)
            )
        )
        print("for_which_city_activities_fields: {0}".format(
            len(for_which_city_activities_fields)
            )
        )
        print("notification_activities_fields: {0}".format(
            len(notification_activities_fields)
            )
        )
        print("result_activities_fields: {0}".format(
            len(result_activities_fields)
            )
        )
        print("comment_activities_fields: {0}".format(
            len(comment_activities_fields)
            )
        )
        print("topic_activities_fields: {0}".format(
            len(topic_activities_fields)
            )
        )
        print("office_activities_fields: {0}".format(
            len(office_activities_fields)
            )
        )
        print("entity_id: {0}".format(
            len(entity_id)
            )
        )
        print("entity: {0}".format(
            len(entity)
            )
        )

        result_info.append(
            activities_id
        )
        result_info.append(
            type_id_activities_id
        )
        result_info.append(
            status_id_activities_id
        )
        result_info.append(
            description_activities_id
        )
        result_info.append(
            start_date_activities_id
        )
        result_info.append(
            end_date_activities_id
        )

        if (len(speaker_activities_fields) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                speaker_activities_fields
            )

        if (len(city_activities_fields) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                city_activities_fields
            )

        if (len(for_whom_activities_fields) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                for_whom_activities_fields
            )

        if (len(format_activities_fields) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                format_activities_fields
            )

        if (len(scale_activities_fields) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                scale_activities_fields
            )

        if (len(name_activities_fields) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                name_activities_fields
            )

        if (len(price_activities_fields) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                price_activities_fields
            )

        if (len(where_activities_fields) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                where_activities_fields
            )

        if (len(translation_link_activities_fields) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                translation_link_activities_fields
            )

        if (len(for_which_city_activities_fields) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                for_which_city_activities_fields
            )

        if (len(notification_activities_fields) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                notification_activities_fields
            )

        if (len(result_activities_fields) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                result_activities_fields
            )

        if (len(comment_activities_fields) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                comment_activities_fields
            )

        if (len(topic_activities_fields) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                topic_activities_fields
            )

        if (len(office_activities_fields) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                office_activities_fields
            )

        result_info.append(
            entity_id
        )

        result_info.append(
            entity
        )

        return result_info

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
