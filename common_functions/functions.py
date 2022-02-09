import re
import yaml
import random as rnd
import json


def counting(
        schedule
        ):
    # Подсчет необходимого количества реквестов
    method = str(schedule).split('(')

    # Для постоянной нагрузки
    if (str(method[0]) == 'const'):
        string = re.split(
            r'[^\w\s]+|[\d]+',
            schedule
        )
        m_or_s = list(
            filter(
                lambda item: item.strip(),
                string
            )
        )
        time = re.findall(
            r'\d+',
            schedule
        )
        time_from = int(time[0])
        time_to = int(time[1])
        if (m_or_s[1] == 'm'):
            duration = time_from * time_to * 60
        else:
            duration = time_from * time_to

    # Для линейной нагрузки
    if (str(method[0]) == 'line'):
        time = re.findall(
            r'\d+',
            schedule
        )
        time_from = int(time[0])
        time_to = int(time[1])
        string = re.split(
            r'[^\w\s]+|[\d]+',
            schedule
        )
        m_or_s = list(
            filter(
                lambda item: item.strip(),
                string
            )
        )
        # if (m_or_s[1] == 'm'):
        #     duration = time_from + time_to * 60
        # else:
        #     duration = time_from + time_to
        duration = 5000000

    # Для ступенчатой нагрузки
    if (str(method[0]) == 'step'):
        time = re.findall(
            r'\d+',
            schedule
        )
        time_from = int(time[0])
        time_to = int(time[1])
        # if (time_from > time_to):
        #     duration = time_from + 5
        # else:
        #     if (time_to > time_from):
        #         duration = time_to + 5
        duration = 5000000

    return duration


# Функция для экранирования
def shielding(
        string
        ):
    return re.sub(r'(["])', r'\\"', string)


# Функция для составления тела запроса
def create_req_string_empty_params(
        service,
        method,
        body
        ):
    req = {
        'service': service,
        'method': method,
        'params': "{}",
        'body': body
    }
    return json.dumps(req)


def create_req_string_empty_body(
        service,
        method,
        params
        ):
    req = {
        'service': service,
        'method': method,
        'params': params,
        'body': "{}"
        }
    return json.dumps(req)


def create_req_string_with_parameters_body(
        service,
        method,
        params,
        body
        ):
    req = {
        'service': service,
        'method': method,
        'params': params,
        'body': body
        }
    return json.dumps(req)


# Функция для записи заголовка в файл
def write_header_to_file(
        file,
        target
        ):
    if (target == 'Test'):
        # для тестового
        file.write(
            '[Authorization: Basic test_local]\n'
        )
        file.write(
            '[Host: ecosystem.esoft.space]\n'
        )
    else:
        if (target == 'Dev'):
            # для девелопа
            file.write(
                '[Authorization: Basic test1]\n'
            )
            file.write(
                '[Host: app.esoft.team]\n'
            )
    file.write(
        '[Content-Type: application/json]\n'
    )
    file.write(
        '[Accept: */*]\n'
    )


# Функция для записи тела запроса в файл
def writing_to_file(
        file,
        req_string
        ):
    file.write(
        str(
            len(
                req_string.encode(
                    'utf-8'
                )
            )
        ) + ' /api\n' + req_string + '\n')


def wildcard_string(
        req_string
        ):
    return str(
        len(
            req_string
        )
    ) + ' /api\n' + req_string + '\n'


def file_writing(
        file,
        req_string
        ):
    file.writelines(
        req_string
    )


# Функция для генеарции файла яндекс-танка load.yaml
def generate_load_yaml(
        target,
        example_file,
        schedule
        ):
    if (target == 'Test'):
        address = 'ecosystem.esoft.space:443'
    if (target == 'Dev'):
        address = 'app.esoft.team:443'

    print('Генерирую load.yaml...')

    yaml_string = """
        overload:
            enabled: true
            package: yandextank.plugins.DataUploader
            token_file: "token.txt"
        phantom:
            enabled: true
            package: yandextank.plugins.Phantom
            address: {0}
            ssl: true
            header_http: "1.1"
            ammo_type: uripost
            ammofile: ExampleAmmo.txt
            writelog: all
            load_profile:
                load_type: rps
                schedule: {1}
        autostop:
            autostop:
                - http(5xx,100%,4s)
        console:
            enabled: true
        telegraf:
            enabled: false
    """.format(
        address,
        schedule
    )
    dict_obj = yaml.safe_load(yaml_string)
    with open('load.yaml', 'w') as yaml_file:
        yaml_file.write(yaml.dump(dict_obj, default_flow_style=False))


# Функция для получения всех комбинаций массива
def combinations(
        a
        ):
    if len(a) == 0:
        return [[]]

    result = []

    for c in combinations(a[1:]):
        result += [c, c+[a[0]]]

    return result


# Определение email или телефон
def is_email(
        contact
        ):

    return (contact.find("@") != -1)


def add_to_list(
        list_of_ammo,
        req_string
        ):
    list_of_ammo.append(
        str(
            len(
                req_string.encode(
                    'utf-8'
                )
            )
        ) + ' /api\n' + req_string + '\n')
    return list_of_ammo


def write_list_to_file(
        file,
        list_of_ammo
        ):
    rnd.shuffle(list_of_ammo)
    for request in list_of_ammo:
        file.write(
            request
        )
