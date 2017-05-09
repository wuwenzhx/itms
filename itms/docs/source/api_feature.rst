.. _api-fea:

Feature
==================

This section introduces feature and its attribute.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Feature List
----------------

We can get feature list by GET method and create feature by POST method.

:Object: Feature
:Authorization: Basic Authorization


:method:`GET`


:Function: Get feature list
:Usage: GET /api/(project_name)/feature/
:Permission: Reader
:Parameters: None
:Response: Feature List
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 77,
            "name": "fea_17",
            "create_time": "2015-10-13T09:04:26Z",
            "owner": "api",
            "component": 61,
            "description": "test",
            "requirement": 194
        },
        {
            "id": 78,
            "name": "fea_78",
            "create_time": "2015-11-10T03:44:24Z",
            "owner": "api",
            "component": 61,
            "description": "test",
            "requirement": 194
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_fea_list():
        url = '{server_add}/api/{project}/feature/'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()


:method:`POST`


:Function: Create new feature
:Usage: POST /api/{project}/feature/
:Permission: Writer
:Parameters:

           {

           'name': 'value',

           'owner': 'value',

           'component': 'value',

           'requirement': 'value',

           'description': 'value'

           }

:Response: New Feature
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "name": "feature",
        "owner": "api",
        "component": 61,
        "description": "test",
        "requirement": 194
    }

:Sample Output:

::

    {
        "id": 79,
        "name": "feature",
        "create_time": "2015-11-12T05:16:25.585484Z",
        "owner": "api",
        "component": 61,
        "description": "test",
        "requirement": 194
    }

:Python Code:

.. code-block:: python
    :linenos:

    def new_fea():
        url = '{server_add}/api/{project}/feature/'.format(server_add=SERVER, project='Media')
        payload = {'name': "feature_test", 'owner': "api", 'component': '61', 'description': "test", 'requirement': '194'}
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.text


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Feature Detail
-------------------

We can get, update and delete a feature with given id.

:Object: Feature
:Authorization: Basic Authorization


:method:`GET`


:Function: Get feature by id
:Usage: GET /api/(project_name)/feature/(id)/
:Permission: Reader
:Parameters: None
:Response: Feature Object
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 79,
        "name": "feature",
        "create_time": "2015-11-12T05:16:25Z",
        "owner": "api",
        "component": 61,
        "description": "test",
        "requirement": 194
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_fea():
        url = '{server_add}/api/{project}/feature/(id)/'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()


:method:`PUT`


:Function: Update feature by id
:Usage: PUT /api/(project_name)/feature/(id)/
:Permission: Writer
:Parameters:

           {

           'name': 'value',

           'owner': 'value',

           'component': 'value',

           'requirement': 'value',

           'description': 'value'

           }

:Response: Feature Object
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "id": 79,
        "name": "feature_new",
        "create_time": "2015-11-12T05:16:25Z",
        "owner": "api new",
        "component": 62,
        "description": "test new",
        "requirement": 195
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_fea():
        url = '{server_add}/api/{project}/feature/(id)/'.format(server_add=SERVER, project='Media')
        print url
        payload = {'name': "feature_new", 'owner': "api new", 'component': '62', 'description': "test new", 'requirement': '195'}
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.text

:method:`DELETE`

:Function: Delete feature by id
:Usage: DELETE /api/(project_name)/feature/(id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    Feature with given id has been removed successfully.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Feature Component List
------------------------

We can get component list by GET method and create component by POST method.

:Object: FeatureComponent
:Authorization: Basic Authorization


:method:`GET`


:Function: Get feature component list
:Usage: GET /api/(project_name)/feature_component/
:Permission: Reader
:Parameters: None
:Response: Feature Component List
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 58,
            "name": "component_58"
        },
        {
            "id": 59,
            "name": "component_2"
        }
    ]


:Python Code:

.. code-block:: python
    :linenos:

    def get_fea_component_list():
        url = '{server_add}/api/{project}/feature_component/'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()


:method:`POST`


:Function: Create new feature component
:Usage: POST /api/(project_name)/feature_component/
:Permission: Writer
:Parameters:

            {

            'name': 'value'

            }

:Response: New Feature Component
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "name": "component"
    }

:Sample Output:

::

    {
        "id": 66,
        "name": "component"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def new_fea_component():
        url = '{server_add}/api/{project}/feature_component/'.format(server_add=SERVER, project='Media')
        payload = {'name': "component"}
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.text


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Feature Component Detail
----------------------------

We can get, update and delete a component with given id.

:Object: FeatureComponent
:Authorization: Basic Authorization


:method:`GET`


:Function: Get feature component by id
:Usage: GET /api/(project_name)/feature_component/(id)/
:Permission: Reader
:Parameters: None
:Response: Feature Component Object
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 66,
        "name": "component"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_fea_component():
        url = '{server_add}/api/{project}/feature_component/(id)'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()


:method:`PUT`


:Function: Update feature component by id
:Usage: PUT /api/(project_name)/feature_component/(id)/
:Permission: Writer
:Parameters:

        {

        'name': 'value'

        }

:Response: Feature Component Object
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "id": 66,
        "name": "component_new"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_fea_component():
        url = '{server_add}/api/{project}/feature_component/(id)/'.format(server_add=SERVER, project='Media')
        print url
        payload = {'name': "component_new"}
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.text


:method:`DELETE`

:Function: Delete feature component by id
:Usage: DELETE /api/{project}/feature_component/(id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    Feature Component with given id has been removed successfully.