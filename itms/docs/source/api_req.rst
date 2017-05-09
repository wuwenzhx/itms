.. _api-req:

Requirement
==================

This section introduces requirement and its attribute.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requirement List
-----------------------

We can get requirement list by GET method and create requirement by POST method.

:Object: Requirement
:Authorization: Basic Authorization


:method:`GET`

:Function: Get requirement list
:Usage: GET /api/(project_name)/requirement/
:Permission: Reader
:Parameters: None
:Response: Requirement List
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 119,
            "name": "requirement_119",
            "create_time": "2015-06-24T16:00:00Z",
            "owner": "xy",
            "type": 42,
            "description": "testcc"
        },
        {
            "id": 120,
            "name": "requirement_120",
            "create_time": "2015-06-25T01:45:25Z",
            "owner": "xy",
            "type": 42,
            "description": "test"
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_req_list():
        url = '{server_add}/api/{project}/requirement/'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()


:method:`POST`

:Function: Create new requirement
:Usage: POST /api/(project_name)/requirement/
:Permission: Writer
:Parameters:

           {

           'name': 'value',

           'owner': 'value',

           'type': 'value',

           'description': 'value'

           }

:Response: New Requirement
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "name": "req_name_new",
        "owner": "api new",
        "type": 42,
        "description": "test new"
    }

:Sample Output:

::

    {
        "id": 119,
        "name": "req_name_new",
        "create_time": "2015-06-24T16:00:00Z",
        "owner": "api new",
        "type": 42,
        "description": "test new"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def create_req():
        url = '{server_add}/api/{project}/requirement/'.format(server_add=SERVER, project='Media')
        payload = {'name': "req_name_new", 'owner': "api new", 'type': '42', 'description': "test new"}
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Requirement Detail
--------------------------

We can get, update and delete a requirement with given id.

:Object: Requirement
:Authorization: Basic Authorization

:method:`GET`

:Function: Get requirement by id
:Usage: GET /api/(project_name)/requirement/(id)/
:Permission: Reader
:Parameters: None
:Response: Requirement Object
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 119,
        "name": "requirement_119",
        "create_time": "2015-06-24T16:00:00Z",
        "owner": "xy",
        "type": 42,
        "description": "testcc"
    }


:Python Code:

.. code-block:: python
    :linenos:

    def get_req():
        url = '{server_add}/api/{project}/requirement/(id)'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()


:method:`PUT`

:Function: Update requirement by id
:Method: PUT /api/(project_name)/requirement/(id)/
:Permission: Writer
:Parameters:

           {

           'name': 'value',

           'owner': 'value',

           'type': 'value',

           'description': 'value'

           }

:Response: Requirement Object
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "id": 119,
        "name": "req_name_new",
        "create_time": "2015-06-24T16:00:00Z",
        "owner": "api new",
        "type": 42,
        "description": "test new"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_req():
        url = '{server_add}/api/{project}/requirement/(id)'.format(server_add=SERVER, project='Media')
        payload = {'name': "req_name_new", 'owner': "api new", 'type': 42, 'description': "test new"}
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()


:method:`DELETE`

:Function: Delete requirement by id
:Usage: DELETE /api/(project_name)/requirement/(id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    Requirement with given id has been removed successfully.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Requirement Type List
-----------------------

We can get requirement type list by GET method and create requirement type name by POST method.


:Object: RequirementType
:Authorization: Basic Authorization

:method:`GET`

:Function: Get requirement type list
:Usage: GET /api/(project_name)/requirement_type/
:Permission: Reader
:Parameters: None
:Response: Requirement Type List
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 47,
            "name": "type_4"
        },
        {
            "id": 48,
            "name": "type_5"
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_req_type_list():
        url = '{server_add}/api/{project}/requirement_type/'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()


:method:`POST`

:Funtion: Create requirement type
:Usage: POST /api/(project_name)/requirement_type/
:Permission: Writer
:parameters:

            {

            'name': 'value'

            }

:Response: New Requirement Type
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "name": "req_type_name"
    }

:Sample Output:

::

    {
        "id": 58,
        "name": "req_type_name_new"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def create_req_type():
        url = '{server_add}/api/{project}/requirement_type/'.format(server_add=SERVER, project='Media')
        payload = {'name': "req_type_name"}
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Requirement Type Detail
------------------------

We can get, update and delete a requirement type with given id.

:Object: RequirementType  
:Authorization: Basic Authorization


:method:`GET`

:Function: Get requirement type by id
:Usage: GET /api/(project_name)/requirement_type/(id)/
:Permission: Reader
:Parameters: None
:Response: Requirement Type Object
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 58,
        "name": "req_type_name"
    }

:Python code:

.. code-block:: python
    :linenos:

    def get_req_type():
        url = '{server_add}/api/{project}/requirement_type/(id)'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()


:method:`PUT`

:Function: Update requirement type by id
:Usage: PUT /api/(project_name)/requirement_type/(id)/
:Permission: Writer
:Parameters:

         {

         'name': 'value'

         }

:Response: Requirement Type Object
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 58,
        "name": "req_type_name_new"
    }

:Python code:

.. code-block:: python
    :linenos:

    def update_req_type():
        url = '{server_add}/api/{project}/requirement_type/(id)'.format(server_add=SERVER, project='Media')
        payload = {'name': "req_type_name_new"}
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()


:method:`DELETE`

:Function: Delete requirement type by id
:Usage: DELETE /api/(project_name)/requirement_type/(id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    Requirement type with given id has been removed successfully.

