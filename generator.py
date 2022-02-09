import os
import sys
import inspect
import time
from attachments import attachments_generator
from catalogs import catalogs_generator
from activities import activities_generator
from addresses import addresses_generator
from objects import objects_generator
from shows import shows_generator
from tasks import tasks_generator
from tickets import tickets_generator
from users import users_generator
import common_functions.functions
from clients import clients_generator
from payments import payments_generator
from documents import documents_generator
from search import search_generator
from activities_business import activities_business_generator
from addresses_business import addresses_business_generator
from attachments_business import attachments_business_generator
from catalogs_business import catalogs_business_generator

currentdir = os.path.dirname(
    os.path.abspath(
        inspect.getfile(
            inspect.currentframe()
        )
    )
)
parentdir = os.path.dirname(
    currentdir
)
sys.path.insert(0, parentdir)


def generate_ammo_method(
        target,
        name_ammo_file,
        schedule,
        service
        ):
    example_file = open(
        name_ammo_file,
        'w'
    )

    common_functions.functions.write_header_to_file(
        example_file,
        target
    )
    duration = common_functions.functions.counting(
        schedule
    )
    print('\nНужно сгенерировать {0} запросов...'.format(
        duration
        )
    )

    print("Генерация патронов...\n")
    count_of_request = 1
    list_of_ammo = []

    start_time = time.time()
    if (service == 'users'):
        count_of_request = users_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'tasks'):
        count_of_request = tasks_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'tickets'):
        count_of_request = tickets_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'objects'):
        count_of_request = objects_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'activities'):
        count_of_request = activities_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'shows'):
        count_of_request = shows_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'addresses'):
        count_of_request = addresses_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'catalogs'):
        count_of_request = catalogs_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'attachments'):
        count_of_request = attachments_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'clients'):
        count_of_request = clients_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'payments'):
        count_of_request = payments_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'documents'):
        count_of_request = documents_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'search'):
        count_of_request = search_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'activities-business'):
        count_of_request = activities_business_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'addresses-business'):
        count_of_request = addresses_business_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'attachments-business'):
        count_of_request = attachments_business_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    if (service == 'catalogs-business'):
        count_of_request = catalogs_business_generator.generate_ammo_method(
            target,
            count_of_request,
            duration,
            example_file,
            list_of_ammo,
            currentdir
        )

    print('\nГенерация патронов заяняла: {0} секунд'.format(
        time.time() - start_time
        )
    )
    print('Количество записанных запросов: {0}'.format(
        count_of_request
        )
    )

    example_file.close()

    common_functions.functions.generate_load_yaml(
        target,
        name_ammo_file,
        schedule
    )


generate_ammo_method(
    'Dev',
    'ExampleAmmo.txt',
    'const(99999,3000m)',
    'catalogs-business'
)
