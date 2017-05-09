.. _api-plan:


Test Plan
===============

This section introduces Testplan and its attribute.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Test Plan List
-----------------

We can get Testplan list by GET method and create Testplan by POST method.

:Object: Testplan
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testplan list
:Usage: GET /api/(project_name)/testplan/
:Permission: Reader
:Parameters: None
:Response: Testplan List
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 81,
            "name": "plan_smta_81",
            "category": 25,
            "performance": true,
            "app": 1,
            "owner": "None",
            "create_time": "2015-09-23T09:16:11Z",
            "start_time": "2015-09-23T09:15:58Z",
            "end_time": "2015-09-23T09:15:58Z",
            "description": "",
            "del_flag": false
        },
        {
            "id": 82,
            "name": "plan_vcsa_82",
            "category": 25,
            "performance": true,
            "app": 2,
            "owner": "None",
            "create_time": "2015-09-23T09:16:49Z",
            "start_time": "2015-09-23T09:16:25Z",
            "end_time": "2015-09-23T09:16:25Z",
            "description": "",
            "del_flag": false
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_testplan_list():
        url = '{server_add}/api/{project}/testplan/'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.url
        print r.status_code
        print r.json()


:method:`POST`

:Function: Create new testplan
:Usage: POST /api/{project}/testplan/
:Permission: Writer
:Parameters:

           {

           'name': 'value',

           'category': 'value',

           'owner': 'value',

           'start_time': 'value',

           'end_time': 'value',

           'description': 'value',

           'performance': 'value',

           'app': 'value'

           }

:Response: New Testplan
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "name": "testplan_perf_1113",
        "category": 25,
        "performance": true,
        "app": 1,
        "owner": "api",
        "start_time": "2015-11-11T09:14:30Z",
        "end_time": "2015-11-11T09:14:30Z",
        "description": "test"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def new_testplan():
        url = '{server_add}/api/{project}/testplan/'.format(server_add=SERVER, project='Media')
        payload = {'name': "perf_testplan", 'category': 25, 'performance': True, 'app': 1, 'owner': "api",
                  'start_time': "2015-11-11T09:14:30Z", 'end_time': "2015-11-11T09:14:30Z", 'description': "test"}
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.url
        print r.status_code
        print r.json()


Test Plan Detail
---------------------

We can get, update and delete a Testplan with given id.

:Object: Testplan
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testplan by id
:Usage: GET /api/(project_name)/testplan/(id)/
:Permission: Reader
:Parameters: None
:Response: Testplan Object
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 128,
        "name": "perf_testplan",
        "category": 25,
        "performance": true,
        "app": 1,
        "owner": "api",
        "create_time": "2015-11-13T08:47:50Z",
        "start_time": "2015-11-11T09:14:30Z",
        "end_time": "2015-11-11T09:14:30Z",
        "description": "test",
        "del_flag": false
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_testplan():
        url = '{server_add}/api/{project}/testplan/(id)/'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.url
        print r.status_code
        print r.json()


:method:`PUT`

:Function: Update testplan by id
:Usage: PUT
:Permission: Writer
:Parameters:

           {

           'name': 'value',

           'category': 'value',

           'owner': 'value',

           'start_time': 'value',

           'end_time': 'value',

           'description': 'value',

           'performance': 'value',

           'app': 'value'

           }

:Response: Testplan Object
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "id": 128,
        "name": "perf_testplan-new",
        "category": 27,
        "performance": true,
        "app": 1,
        "owner": "api_new",
        "start_time": "2015-11-14T09:14:30Z",
        "end_time": "2015-11-14T09:14:30Z",
        "description": "test_new"
    }

.. note:: Cannot update 'performance' and 'app'.

:Python Code:

.. code-block:: python
    :linenos:

    def update_testplan():
        url = '{server_add}/api/{project}/testplan/(id)/'.format(server_add=SERVER, project='Media')
        payload = {'name': "perf_testplan_new_new", 'category': 26, 'performance': True, 'app': 1, 'owner': "api",
                  'start_time': "2015-11-15T09:14:30Z", 'end_time': "2015-11-15T09:14:30Z", 'description': "test"}
        print payload
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.url
        print r.status_code
        print r.json()


:method:`DELETE`

:Function: Delete testplan by id
:Usage: DELETE /api/{project}/testplan/(id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    Testplan with given id has been removed successfully.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Plan Category List
----------------------------

We can get category list by GET method and create component by POST method.

:Object: TestplanCategory
:Authorization: Basic Authorization


:method:`GET`

:Function: Get testplan category list
:Usage: GET /api/(project_name)/testplan_category/
:Permission: Reader
:Parameters: None
:Response: Testplan Category List
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 25,
            "name": "Regular"
        },
        {
            "id": 26,
            "name": "Undated"
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_category_list():
        url = '{server_add}/api/{project}/testplan_category/'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.url
        print r.status_code
        print r.json()


:method:`POST`

:Function: Create new testplan category
:Usage: POST /api/{project}/testplan_category/
:Permission: Writer
:Parameters:

             {

             'name': 'value'

             }

:Response: New Testplan Category
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "name": "category"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def new_category():
        url = '{server_add}/api/{project}/testplan_category/'.format(server_add=SERVER, project='Media')
        payload = {'name': "category"}
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.url
        print r.status_code
        print r.json()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Test Plan Category Detail
----------------------------

We can get, update and delete a category with given id.

:Object: TestplanCategory
:Authorization: Basic Authorization


:method:`GET`

:Function: Get testplan category by id
:Usage: GET /api/(project_name)/testplan_category/(id)/
:Permission: Reader
:Parameters: None
:Response: Testplan Category Object
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 36,
        "name": "category"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_category():
        url = '{server_add}/api/{project}/testplan_category/(id)/'.format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.url
        print r.status_code
        print r.json()


:method:`PUT`

:Function: Update testplan category by id
:Usage: PUT /api/{project}/testplan_category/(id)/
:Permission: Writer
:Parameters:

             {

             'name': 'value'

             }

:Response: Testplan Category Object
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "id": 36,
        "name": "category_new"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_category():
        url = '{server_add}/api/{project}/testplan_category/(id)/'.format(server_add=SERVER, project='Media')
        payload = {'name': "category_new"}
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print r.url
        print r.status_code
        print r.json()


:method:`DELETE`

:Function: Delete testplan category by id
:Usage: DELETE /api/{project}/testplan_category/(id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

 Category with given id has been removed successfully.
