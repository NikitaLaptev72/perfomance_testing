import requests
import base64
import json
from dotenv import dotenv_values


def auth(
            target,
            currentdir
        ):
    client_str = '{0} {1}'.format(
        dotenv_values(f'{currentdir}/.env_oauth_{target.lower()}').get('client_id'),
        dotenv_values(f'{currentdir}/.env_oauth_{target.lower()}').get('client_secret')
    )
    session_url = dotenv_values(f'{currentdir}/.env_oauth_{target.lower()}').get('session_url')

    auth = base64.b64encode(client_str.encode("utf-8"))

    access_request = requests.post(
        url=dotenv_values(f'{currentdir}/.env_oauth').get('access_url'),
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic {0}'.format(
                auth.decode("utf-8")
            )
        },
        data={
            'grant_type': 'password',
            'username': dotenv_values(f'{currentdir}/.env_oauth').get('username'),
            'password': dotenv_values(f'{currentdir}/.env_oauth').get('password')
        }
    )

    data = {
        'accessToken': json.loads(access_request.text)["access_token"],
        'refreshToken': json.loads(access_request.text)["refresh_token"],
        'noredirect': 'true'
    }

    session_request = requests.get(
        session_url,
        data,
        verify=False
    )

    return json.loads(session_request.text)["sessionId"]
