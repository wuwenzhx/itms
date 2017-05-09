.. _api-case:


Test Case
========================

This section introduces Testcase and its attribute.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Case List
-------------------

We can get test case list by GET method and create test suite by POST method.

:Object: Testcase
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testcase list
:Usage: GET /api/(project_name)/testcase/
:Permission: Reader
:Parameters: None
:Response: Testcase List
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 45,
            "name": "case_normal",
            "type": 20,
            "description": "test",
            "script_path": "xxxxxx",
            "config_path": "xxxxxx",
            "parameters": "xxxxxx",
            "feature": 10,
            "testsuite": [
                7,
                8
            ],
            "performance": false,
            "app": null,
            "del_flag": false
        },
        {
            "id": 50,
            "name": "case_perf_1",
            "type": 20,
            "description": "xxxxxx",
            "script_path": "xxxxxx",
            "config_path": "xxxxxx",
            "parameters": "xxxxxx",
            "feature": 9,
            "testsuite": [
                56,
                57,
                121
            ],
            "performance": true,
            "app": 1,
            "del_flag": false
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_testcase_list():
        url = ('{server_add}/api/{project}/testcase/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`POST`

:Function: Create new testcase
:Usage: POST /api/{project}/testcase/
:Permission: Writer
:Parameters:

           {

           'name': 'value',

           'type': 'value',

           'script_path': 'value',

           'config_path': 'value',

           'parameters': 'value',

           'feature': 'value',

           'testsuite': 'value',

           'description': 'value',

           'performance': 'value',

           'app': 'value'

           }

:Response: New Testcase
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "name": "case_normal",
        "type": 20,
        "description": "test",
        "script_path": "xxxxxx",
        "config_path": "xxxxxx",
        "parameters": "xxxxxx",
        "feature": 80,
        "testsuite": [
            119
        ],
        "performance": false,
        "app": null
    }

:Python Code:

.. code-block:: python
    :linenos:

    def new_testcase():
        url = ('{server_add}/api/{project}/testcase/').format(server_add=SERVER, project='Media')
        payload = {'name':"case_normal_1117", 'type':20, 'description':"xxxxxx", 'script_path':"xxxxxx", 'config_path':"xxx",
                   'parameters':"xxxxxx", 'feature':80, 'testsuite':[119], 'performance':False, 'app':None}
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Case Detail
-------------------

We can get, update and delete a Testcase with given id.

:Object: Testcase
:Authorization: Basic Authorization


:method:`GET`

:Function: Get testcase by id
:Usage: GET /api/(project_name)/testcase/(id)/
:Permission: Reader
:Parameters: None
:Response: Testcase Object
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 181,
        "name": "case_normal",
        "type": 20,
        "description": "xxxxxx",
        "script_path": "xxxxxx",
        "config_path": "xxx",
        "parameters": "xxxxxx",
        "feature": 80,
        "testsuite": [
            119
        ],
        "performance": false,
        "app": null,
        "del_flag": false
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_testcase():
        url = ('{server_add}/api/{project}/testcase/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`PUT`

:Function: Update testcase by id
:Method: PUT
:Permission: Writer
:Parameters:

           {

           'name': 'value',

           'type': 'value',

           'script_path': 'value',

           'config_path': 'value',

           'parameters': 'value',

           'feature': 'value',

           'testsuite': 'value',

           'description': 'value',

           'performance': 'value',

           'app': 'value'

           }

:Response: Testcase Object
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "name": "case_normal_new",
        "type": 25,
        "description": "test",
        "script_path": "test",
        "config_path": "test",
        "parameters": "test",
        "feature": 79,
        "testsuite": [
            118
        ],
        "performance": false,
        "app": null
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_testcase():
        url = ('{server_add}/api/{project}/testcase/(id)/').format(server_add=SERVER, project='Media')
        payload = {'name':"case_normal_new", 'type':25, 'description':"test", 'script_path':"test", 'config_path':"test",
        'parameters':"test", 'feature':79, 'testsuite':[118], 'performance':False, 'app':None}
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`DELETE`

:Function: Delete testcase by id
:Usage: DELETE /api/{project}/testcase/(id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
:Sample Output:

::

 Testcase with given id has been removed successfully.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Case Type List
-------------------------

We can get testcase type list by GET method and create testcase type name by POST method.

:Object: TestcaseType
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testcase type list
:Usage: GET /api/(project_name)/testcase_type/
:Permission: Reader
:Parameters: None
:Response: Testcase Type List
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 20,
            "name": "case_type_1"
        },
        {
            "id": 21,
            "name": "case_type_2"
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_case_type_list():
        url = ('{server_add}/api/{project}/testcase_type/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`POST`

:Function: Create new testcase type
:Usage: POST /api/{project}/testcase_type/
:Permission: Writer
:Parameters:

         {

         'name': 'value'

         }

:Response: New Testcase Type
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "name": "case_type"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def new_case_type():
        url = ('{server_add}/api/{project}/testcase_type/').format(server_add=SERVER, project='Media')
        payload = {'name':"case_type"}
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Case Type Detail
-------------------------

We can get, update and delete a testcase type with given id.

:Object: TestcaseType
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testcase type by id
:Usage: GET /api/(project_name)/testcase_type/(id)/
:Permission: Reader
:Parameters: None
:Response: Testcase Type Object
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 27,
        "name": "case_type"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_testcase_type():
        url = ('{server_add}/api/{project}/testcase_type/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`PUT`

:Function: Update testcase type by id
:Usage: PUT /api/{project}/testcase_type/(id)/
:Permission: Writer
:Parameters:

         {

         'name': 'value'

         }

:Response: Testcase Type Object
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "id": 27,
        "name": "case_type_new"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_case_type():
        url = ('{server_add}/api/{project}/testcase_type/(id)/').format(server_add=SERVER, project='Media')
        payload = {'name':"case_type_new"}
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`DELETE`

:Function: Delete testcase type by id
:Usage: DELETE /api/{project}/testcase_type/(id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

 Testcase type with given id has been removed successfully.
