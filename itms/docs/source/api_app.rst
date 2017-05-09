.. _api-app:


APP
===============

This section introduces APP and its attributes.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

APP List
---------------

We can get App list by GET method and create App by POST method.

:Object: App
:Authorization: Basic Authorization

:method:`GET`

:Function: Get app list
:Usage: GET /api/(project_name)/app/
:Permission: Reader
:Parameters: None
:Response: app list
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 1,
            "name": "SMTA"
        },
        {
            "id": 2,
            "name": "VCSA"
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_app_list():
        url = '{server_add}/api/{project}/app/'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()

:method:`POST`

:Function: Create new app
:Usage: POST /api/(project_name)/app/
:Permission: Writer
:Parameters:

            {

            'name':'value'

            }

:Response: New app 
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "name": "TEST"
    }

:Sample Output:

::

    {
        "id": 10,
        "name": "TEST"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def new_app():
        url = '{server_add}/api/{project}/app/'.format(server_add=SERVER, project='Media')
        payload = {'name': "TEST_new"}
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.text

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

APP Detail
---------------

We can get, update and delete an App with given id.

:Object: App
:Authorization: Basic Authorization

:method:`GET`

:Function: Get app by id
:Usage: GET /api/(project_name)/app/(app_id)/
:Permission: Reader
:Parameters: None
:Response: app
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 10,
        "name": "TEST"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_app():
        url = '{server_add}/api/{project}/app/(id)/'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()

:method:`PUT`

:Function: Update app by id
:Usage: PUT /api/{project}/app/(id)
:Permission: Writer
:Parameters:

        {

        'name': 'value'

        }

:Response: app
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "id": 10,
        "name": "TEST_new"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_app():
        url = '{server_add}/api/{project}/app/(id)/'.format(server_add=SERVER, project='Media')
        print url
        payload = {'name': "TEST_new"}
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.text

:method:`DELETE`

:Function: Delete app by id
:Usage: DELETE /api/{project}/app/(id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    APP with given id has been removed successfully.

.. note:: Cannot delete an APP in use.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

APP Attribute List
-----------------------

We can get App attribute list by GET method and create App attribute by POST method.

:Object: App Attr
:Authorization: Basic Authorization


:method:`GET`

:Function: Get app attr list
:Usage: GET /api/(project_name)/app_attr/
:Permission: Reader
:Parameters: None
:Response: app attr list
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 1,
            "name": "ChannelNum",
            "app": 1
        },
        {
            "id": 2,
            "name": "FPS",
            "app": 1
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_appattr_list():
        url = '{server_add}/api/{project}/app_attr/'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()


:method:`POST`

:Function: Create new app attr
:Usage: POST /api/{project}/app_attr/
:Permission: Writer
:Parameters:

           {

           'name':'value',

           'app': 'value

           }

:Response: New app attr 
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "name": "ATTR",
        "app": 1
    }

:Python Code:

.. code-block:: python
    :linenos:

    def new_appattr():
        url = '{server_add}/api/{project}/app_attr/'.format(server_add=SERVER, project='Media')
        payload = {'name': "ATTR", 'app': '1'}
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.text


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

APP Attribute Detail
-----------------------

We can get, update and delete an App attribute with given id.

:Object: App Attr
:Authorization: Basic Authorization


:method:`GET`

:Function: Get app attr by id
:Usage: GET /api/(project_name)/app_attr/(appattr_id)/
:Permission: Reader
:Parameters: None
:Response: app attr
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 71,
        "name": "ATTR",
        "app": 1
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_appattr():
        url = '{server_add}/api/{project}/app_attr/(id)/'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()


:method:`PUT`

:Function: Update app attr by id
:Usage: PUT /api/(project_name)/app_attr/(appattr_id)/
:Permission: Writer
:Parameters:

           {

           'name': 'value',

           'app': 'value'

           }

:Response: app attr
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "id": 71,
        "name": "ATTR_new",
        "app": 1
    }

.. note:: parameter 'app' can not be changed.


:Python Code:

.. code-block:: python
    :linenos:

    def update_appattr():
        url = '{server_add}/api/{project}/app_attr/(id)/'.format(server_add=SERVER, project='Media')
        print url
        payload = {'name': "TEST_1113", 'app': '1'}
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.text


:method:`DELETE`

:Function: Delete app attr by id
:Usage: DELETE /api/(project_name)/app_attr/(appattr_id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    APP attribute with given id has been removed successfully.

.. note:: Cannot delete an attribute in use.