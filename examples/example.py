# SPDX-License-Identifier: Apache-2.0
#
# Copyright (c) 2023 Smallstep Labs, Inc <techadmin@smallstep.com> All Rights Reserved.

from smallstep import api
from smallstep.exceptions import StepException


def main():
    smallstep_api_host = "https://gateway.smallstep.com/api"
    smallstep_api_token = "your_smallstep_api_token"

    # You can pass the smallstep_api_host and smallstep_api_token directly into the class initialiser.
    # This takes priority over all other settings.
    # This uses the .to_dict() function to return a dictionary from the list of authorities.
    try:
        print("Get all authorities (Class initialiser):")
        authorities = api.StepAuthority(smallstep_api_host=smallstep_api_host, smallstep_api_token=smallstep_api_token)
        auths = authorities.get_all()
        for auth in auths:
            print(auth.to_dict())
    except StepException as e:
        print(e.headers)
        print(e.status_code)
        print(e.message)

    # or you can set SMALLSTEP_API_HOST and SMALLSTEP_API_TOKEN.
    # These will be used without having to pass arguments into the class
    # Environment vars take second priority
    # or you can create a .env file in the directory of your code and this will be used.
    # See examples/dot_env for an example.
    # a .env file takes third priority
    # This just returns the Authority() model object
    try:
        print("Get all authorities (Env vars):")
        authorities = api.StepAuthority()
        print(authorities.get_all())
    except StepException as e:
        print(e.headers)
        print(e.status_code)
        print(e.message)

    # This example shows what is returned by StepException
    # Headers(
    #     {
    #         "date": "Tue, 10 Oct 2023 19:17:46 GMT",
    #         "content-type": "application/json; charset=utf-8",
    #         "content-length": "28",
    #         "connection": "keep-alive",
    #         "x-request-id": "3d88027b016bc6fdd862b6c7487da709",
    #         "strict-transport-security": "max-age=15724800; includeSubDomains",
    #     }
    # )
    # 401
    # {'message': 'Invalid token'}

    try:
        print("Get all authorities (Bad API token):")
        authorities = api.StepAuthority(smallstep_api_token="WrongToken")
        print(authorities.get_all())
    except StepException as e:
        print(e.headers)
        print(e.status_code)
        print(e.message)


if __name__ == "__main__":
    main()
