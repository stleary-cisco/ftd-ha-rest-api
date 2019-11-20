"""
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

"""

import json

import requests


def get_licenses(host, port, access_token):
    """
    Sends a GET request to obtain all licenses from server
    :param host: ftd host address
    :param port: ftd port
    :param access_token: OAUTH access token
    """
    smart_licenses_path = "api/fdm/latest/license/smartlicenses"
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer {}".format(access_token)
    }

    url = "https://{host}:{port}/{url}".format(host=host, port=port, url=smart_licenses_path)
    print("Send a GET request to url: {}".format(url))
    response = requests.get(url, verify=False, headers=headers)

    if response.status_code != 200:
        print("Failed with status {}: {}".format(response.status_code, json.dumps(response.json(), indent=2)))
        raise Exception("Failed to get licenses.")

    print(json.dumps(response.json(), indent=2))
    return response.json()["items"]


def post_licenses(host, port, access_token, smart_license):
    """
    Requires Python v3.0 or greater and requests lib.
    Sends a POST request to create specified license
    :param host: ftd host address
    :param port: ftd port
    :param access_token: OAUTH access token
    :param smart_license: object representing Smart License model
    """
    smart_licenses_path = "api/fdm/latest/license/smartlicenses"
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer {}".format(access_token),
        "Content-Type": "application/json"
    }

    url = "https://{host}:{port}/{url}".format(host=host, port=port, url=smart_licenses_path)
    print("Send a POST request to url: {}".format(url))
    response = requests.post(url, data=json.dumps(smart_license), verify=False, headers=headers)

    if response.status_code != 200:
        print("Failed with status {}: {}".format(response.status_code, json.dumps(response.json(), indent=2)))
        raise Exception("Failed to enable license: {}".format(json.dumps(smart_license)))

    print(json.dumps(response.json(), indent=2))

    return response.json()


def delete_license(host, port, access_token, smart_license_id):
    """
    Requires Python v3.0 or greater and requests lib.
    Sends a DELETE request to remove specified license by id
    :param host: ftd host address
    :param port: ftd port
    :param access_token: OAUTH access token
    :param smart_license_id: id of the created license object
    """
    smart_licenses_path = "api/fdm/latest/license/smartlicenses"
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer {}".format(access_token)
    }

    url = "https://{host}:{port}/{url}/{license_id}".format(host=host, port=port, url=smart_licenses_path,
                                                            license_id=smart_license_id)
    print("Send a DELETE request to url: {}".format(url))
    response = requests.delete(url, verify=False, headers=headers)

    if response.status_code != 204:
        print("Failed with status {}: {}".format(response.status_code, json.dumps(response.json(), indent=2)))
        raise Exception("Failed to delete license.")

    print("License deleted successfully. License ID: {}".format(smart_license_id))


def get_license_by_type(host, port, access_token, smart_license_type):
    """
    Returns license from server by type

    ``smart_license_type`` parameter accepts the following values:
        ``BASE`` - perpetual license is included with the purchase of the system;
        ``THREAT`` - allows you to perform intrusion detection and prevention and file control;
        ``MALWARE`` - allows you to perform Cisco Advanced Malware Protection (AMP);
        ``URLFILTERING`` - allows you to control web access based on URL categories and reputations;
        ``PLUS``, ``APEX`` or ``VPNOnly`` - RA VPN license types.

    :param host: ftd host address
    :param port: ftd port
    :param access_token: OAUTH access token
    :param smart_license_type: Smart License type (e.g. APEX)
    """
    smart_licenses = get_licenses(host, port, access_token)
    return next((smart_license for smart_license in smart_licenses
                 if smart_license["licenseType"] == smart_license_type), None)
