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
            database=dotenv_values(f"{currentdir}/.env_databases").get('objects_database')
        )
        connection_for_adresses = psycopg2.connect(
            user=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('user'),
            password=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('password'),
            host=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('host'),
            port=dotenv_values(f"{currentdir}/.env_{target.lower()}").get('port'),
            database=dotenv_values(f"{currentdir}/.env_databases").get('addresses_database')
        )

        cursor = connection_for_adresses.cursor()

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

        cursor.close()

        cursor = connection.cursor()

        print('Получаю cottage_settlements_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"cottageSettlements\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        cottage_settlements_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю developer_id_cottage_settlements_id...')
        cursor.execute('''SELECT DISTINCT \"developerId\"
            from \"cottageSettlements\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        developer_id_cottage_settlements_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю road_cottage_settlements_id...')
        cursor.execute('''SELECT DISTINCT \"road\"
            from \"cottageSettlements\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        road_cottage_settlements_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю land_purpose_cottage_settlements_id...')
        cursor.execute('''SELECT DISTINCT \"landPurpose\"
            from \"cottageSettlements\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        land_purpose_cottage_settlements_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю status_cottage_settlements_id...')
        cursor.execute('''SELECT DISTINCT \"status\"
            from \"cottageSettlements\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        status_cottage_settlements_id = list(
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

        print('Получаю status_object_ids...')
        cursor.execute('''SELECT DISTINCT \"status\"
            from \"objects\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        status_object_ids = list(
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

        print('Получаю cadastr_object_ids...')
        cursor.execute('''SELECT DISTINCT \"cadastr\"
            from \"objects\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        cadastr_object_ids = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю personal_account_object_ids...')
        cursor.execute('''SELECT DISTINCT \"personalAccount\"
            from \"objects\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        personal_account_object_ids = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю new_building_owner_type_object_ids...')
        cursor.execute('''SELECT DISTINCT \"newBuildingOwnerType\"
            from \"objects\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        new_building_owner_type_object_ids = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю entrances_id...')
        cursor.execute('''SELECT DISTINCT \"id\" from \"entrances\" LIMIT 30000 ''')
        result = cursor.fetchall()
        entrances_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю general_plan_entrances_id...')
        cursor.execute('''SELECT DISTINCT \"generalPlanId\" from \"entrances\" LIMIT 30000 ''')
        result = cursor.fetchall()
        general_plan_entrances_id = list(
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

        print('Получаю housing_complex_general_plans_id...')
        cursor.execute('''SELECT DISTINCT \"housingComplexId\"
            from \"generalPlans\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        housing_complex_general_plans_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю history_keys_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"historyKeys\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        history_keys_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю keys_id_history_keys_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"keys\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        keys_id_history_keys_id = list(
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

        print('Получаю developer_housing_complexes_id...')
        cursor.execute('''SELECT DISTINCT \"developer\"
            from \"housingComplexes\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        developer_housing_complexes_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю general_plans_installment_terms_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"generalPlansInstallmentTerms\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        general_plans_installment_terms_id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю keys_Id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"keys\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        keys_Id = list(
            sum(
                result,
                ()
            )
        )

        print('Получаю promotions_id...')
        cursor.execute('''SELECT DISTINCT \"id\"
            from \"promotions\" where \"deletedAt\" IS NULL LIMIT 30000''')
        result = cursor.fetchall()
        promotions_id = list(
            sum(
                result,
                ()
            )
        )

        print("\nВсего получено записей:")
        print("cottage_settlements_id: {0}".format(
            len(cottage_settlements_id)
            )
        )
        print("adresses_id: {0}".format(
            len(adresses_id)
            )
        )
        print("developer_id_cottage_settlements_id: {0}".format(
            len(developer_id_cottage_settlements_id)
            )
        )
        print("road_cottage_settlements_id: {0}".format(
            len(road_cottage_settlements_id)
            )
        )
        print("land_purpose_cottage_settlements_id: {0}".format(
            len(land_purpose_cottage_settlements_id)
            )
        )
        print("status_cottage_settlements_id: {0}".format(
            len(status_cottage_settlements_id)
            )
        )
        print("object_ids: {0}".format(
            len(object_ids)
            )
        )
        print("status_object_ids: {0}".format(
            len(status_object_ids)
            )
        )
        print("class_object_ids: {0}".format(
            len(class_object_ids)
            )
        )
        print("type_object_ids: {0}".format(
            len(type_object_ids)
            )
        )
        print("cadastr_object_ids: {0}".format(
            len(cadastr_object_ids)
            )
        )
        print("personal_account_object_ids: {0}".format(
            len(personal_account_object_ids)
            )
        )
        print("new_building_owner_type_object_ids: {0}".format(
            len(new_building_owner_type_object_ids)
            )
        )
        print("entrances_id: {0}".format(
            len(entrances_id)
            )
        )
        print("general_plan_entrances_id: {0}".format(
            len(general_plan_entrances_id)
            )
        )
        print("general_plans_id: {0}".format(
            len(general_plans_id)
            )
        )
        print("housing_complex_general_plans_id: {0}".format(
            len(housing_complex_general_plans_id)
            )
        )
        print("history_keys_id: {0}".format(
            len(history_keys_id)
            )
        )
        print("keys_id_history_keys_id: {0}".format(
            len(keys_id_history_keys_id)
            )
        )
        print("housing_complexes_id: {0}".format(
            len(housing_complexes_id)
            )
        )
        print("developer_housing_complexes_id: {0}".format(
            len(developer_housing_complexes_id)
            )
        )
        print("general_plans_installment_terms_id: {0}".format(
            len(general_plans_installment_terms_id)
            )
        )
        print("keys_Id: {0}".format(
            len(keys_Id)
            )
        )
        print("promotions_id: {0}".format(
            len(keys_Id)
            )
        )

        if (len(cottage_settlements_id) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                cottage_settlements_id
            )

        result_info.append(
                adresses_id
            )

        if (len(developer_id_cottage_settlements_id) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                developer_id_cottage_settlements_id
            )

        if (len(road_cottage_settlements_id) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                road_cottage_settlements_id
            )

        if (len(land_purpose_cottage_settlements_id) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                land_purpose_cottage_settlements_id
            )

        if (len(status_cottage_settlements_id) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                status_cottage_settlements_id
            )

        result_info.append(
            object_ids
        )
        result_info.append(
            status_object_ids
            )
        result_info.append(
            class_object_ids
            )
        result_info.append(
            type_object_ids
            )
        result_info.append(
            cadastr_object_ids
            )
        result_info.append(
            personal_account_object_ids
            )
        result_info.append(
            new_building_owner_type_object_ids
            )
        result_info.append(
            entrances_id
            )
        result_info.append(
            general_plan_entrances_id
            )
        result_info.append(
            general_plans_id
            )
        result_info.append(
            housing_complex_general_plans_id
            )
        result_info.append(
            history_keys_id
            )
        result_info.append(
            keys_id_history_keys_id
            )
        result_info.append(
            housing_complexes_id
            )

        if (len(general_plans_installment_terms_id) == 0):
            result_info.append(
                ['1']
            )
        else:
            result_info.append(
                general_plans_installment_terms_id
            )

        result_info.append(
            developer_housing_complexes_id
            )
        result_info.append(
            keys_Id
            )
        result_info.append(
            promotions_id
            )

        return result_info

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
