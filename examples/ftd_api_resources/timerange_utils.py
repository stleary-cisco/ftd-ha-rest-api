'''
Copyright (c) 2019 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). A copy of the License
can be found in the LICENSE.TXT file of this software or at
https://developer.cisco.com/site/license/cisco-sample-code-license/
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
express or implied.
'''

import json
import requests


def get_all_time_range(host, port, access_token):
    """
    Requires Python v3.0 or greater and requests lib.
    Send time range objects GETALL request.
    :param host: ftd host address
    :param port: ftd port
    :param access_token: OAUTH token for device access
    :return: time-range objects
    """
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer {}".format(access_token)
    }
    timerange_objects = None
    tro_url = 'api/fdm/latest/object/timeranges'
    response = requests.get(
        'https://{host}:{port}/{url}'.format(host=host, port=port, url=tro_url),
        verify=False, headers=headers)
    if response.status_code != 200:
        print("Failed GET time range objects response {} {}".format(response.status_code, response.json()))
    else:
        timerange_objects = response.json().get('items')
        print('time range objects found: {}'.format(str(timerange_objects)))
    return timerange_objects


def post_time_range(host, port, access_token, tro_object):
    """
    Requires Python v3.0 or greater and requests lib.
    Send a time range object POST request.
    :param host: ftd host address
    :param port: ftd port
    :param access_token: OAUTH token for device access
    :param tro_object: object representing the time-range
    :return: time-range object
    """
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer {}".format(access_token)
    }
    tro_url = 'api/fdm/latest/object/timeranges'
    response = requests.post(
        'https://{host}:{port}/{url}'.format(host=host, port=port, url=tro_url),
        data=json.dumps(tro_object), verify=False, headers=headers)
    if response.status_code != 200:
        print("Failed POST time range object response {} {}".format(response.status_code, response.json()))
        tro_object = None
    else:
        print(response.json())
        tro_object = response.json()
    return tro_object


def update_time_range(host, port, access_token, tro_id, tro_object_update):
    """
    Requires Python v3.0 or greater and requests lib.
    Send a time range object PUT request.
    :param host: ftd host address
    :param port: ftd port
    :param access_token: OAUTH token for device access
    :param tro_id: unique identifier for a time-range object
    :param tro_object_update: updated time-range object
    :return: time-range object
    """
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer {}".format(access_token)
    }
    tro_url = 'api/fdm/latest/object/timeranges/{}'.format(tro_id)
    response = requests.put(
        'https://{host}:{port}/{url}'.format(host=host, port=port, url=tro_url),
        data=json.dumps(tro_object_update), verify=False, headers=headers)
    if response.status_code != 200 and response.status_code != 204:
        print("Failed PUT time-range object response {} {}".format(response.status_code, response.json()))
        tro_object_update = None
    elif response.status_code == 200:
        print(response.json())
        tro_object_update = response.json()
    return tro_object_update


def get_time_range(host, port, access_token, tro_id):
    """
    Requires Python v3.0 or greater and requests lib.
    Send a time range object GET request.
    :param host: ftd host address
    :param port: ftd port
    :param access_token: OAUTH token for device access
    :param tro_id: unique identifier for a time-range object
    :return: time-range object
    """
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer {}".format(access_token)
    }
    timerange_object = None
    tro_url = 'api/fdm/latest/object/timeranges/{}'.format(tro_id)
    response = requests.get(
        'https://{host}:{port}/{url}'.format(host=host, port=port, url=tro_url),
        verify=False, headers=headers)
    if response.status_code != 200:
        print("Failed GET time range objects response {} {}".format(response.status_code, response.json()))
    else:
        timerange_object = response.json()
        print('time range object found: {}'.format(str(timerange_object)))
    return timerange_object


def delete_time_range(host, port, access_token, tro_id):
    """
    Requires Python v3.0 or greater and requests lib.
    Send a time range object DELETE request.
    :param host: ftd host address
    :param port: ftd port
    :param access_token: OAUTH token for device access
    :param tro_id: unique identifier for time-range object
    :return: response status code
    """
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer {}".format(access_token)
    }
    status_code_for_delete_operation = None
    tro_url = 'api/fdm/latest/object/timeranges/{}'.format(tro_id)
    response = requests.delete(
        'https://{host}:{port}/{url}'.format(host=host, port=port, url=tro_url),
        verify=False, headers=headers)
    if response.status_code != 204:
        print("Failed DELETE time range object response {} {}".format(response.status_code, response.json()))
    else:
        status_code_for_delete_operation = response.status_code
        print('time range object is deleted, error code is: {}'.format(status_code_for_delete_operation))
    return status_code_for_delete_operation