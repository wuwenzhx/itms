.. _api-suite:


Test Suite
========================

This section introduces Testsuite and its attribute.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Suite List
--------------------

We can get test suite list by GET method and create test suite by POST method.


:Object: Testsuite
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testsuite list
:Usage: GET /api/(project_name)/testsuite/
:Permission: Reader
:Parameters: None
:Response: Testsuite List
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 43,
            "name": "suite_12",
            "subsystem": 2,
            "performance": false,
            "app": null,
            "description": "",
            "testplan": [
                18,
                84
            ],
            "del_flag": false
        },
        {
            "id": 56,
            "name": "suite_perf_1",
            "subsystem": 2,
            "performance": true,
            "app": 1,
            "description": "",
            "testplan": [
                80,
                81
            ],
            "del_flag": false
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_testsuite_list():
        url = ('{server_add}/api/{project}/testsuite/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`POST`

:Function: Create new testsuite
:Usage: POST /api/(project_name)/testsuite/
:Permission: Writer
:Parameters:

           {

           'name': 'value',

           'subsystem': 'value',

           'testplan': 'value',

           'description': 'value',

           'performance': 'value',

           'app': 'value'

           }

:Response: New Testsuite
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "name": "testsuite_perf",
        "subsystem": 2,
        "performance": true,
        "app": 1,
        "description": "test",
        "testplan": [
            126, 124
        ]
    }

:Python Code:

.. code-block:: python
    :linenos:

    def new_testsuite():
        url = ('{server_add}/api/{project}/testsuite/').format(server_add=SERVER, project='Media')
        payload = {'name':"testsuite_perf", 'subsystem':'2', 'performance':True, 'app':'1', 'description':"test",
                   'testplan':[126, 124]}
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

.. note:: "plan:(id) not match test suite of performance type" show if Testsuite and Testplan don't have the same performance setting.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Suite Detail
------------------------

We can get, update and delete a Testsuite with given id.

:Object: Testsuite
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testsuite by id
:Usage: GET /api/(project_name)/testsuite/(id)/
:Permission: Reader
:Parameters: None
:Response: Testsuite Object
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 123,
        "name": "testsuite_perf",
        "subsystem": 2,
        "performance": true,
        "app": 1,
        "description": "test",
        "testplan": [
            124,
            126
        ],
        "del_flag": false
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_testsuite():
        url = ('{server_add}/api/{project}/testsuite/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`PUT`

:Function: Update testsuite by id
:Usage: PUT /api/(project_name)/testsuite/(id)/
:Permission: Writer
:Parameters:

           {

           'name': 'value',

           'subsystem': 'value',

           'testplan': 'value',

           'description': 'value',

           'performance': 'value',

           'app': 'value'

           }

:Response: Testsuite Object
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "id": 123,
        "name": "testsuite_perf_new",
        "subsystem": 4,
        "performance": true,
        "app": 1,
        "description": "test new",
        "testplan": [
            126
        ]
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_testsuite():
        url = ('{server_add}/api/{project}/testsuite/(id)/').format(server_add=SERVER, project='Media')
        payload = {'name':"testsuite_perf_new", 'subsystem':'4', 'performance':True, 'app':'1', 'description':"test_new",
                   'testplan':[126]}
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

.. note:: "Not allow change performance and app attribute" shows when try to change performance and app.


:method:`DELETE`

:Function: Delete testsuite by id
:Usage: DELETE /api/{project}/testsuite/(id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
:Sample Output:

::

 Testsuite with given id has been removed successfully.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Suite Subsystem List
--------------------------

We can get subsystem list by GET method and create subsystem by POST method.

:Object: TestsuiteSubsystem
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testsuite subsystem list
:Usage: GET /api/(project_name)/testsuite_subsystem/
:Permission: Reader
:Parameters: None
:Response: Testsuite Subsystem List
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 2,
            "name": "subsystem_1"
        },
        {
            "id": 4,
            "name": "subsystem_3"
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_subsystem_list():
        url = ('{server_add}/api/{project}/testsuite_subsystem/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`POST`

:Function: Create new testsuite subsystem
:Usage: POST /api/{project}/testsuite_subsystem/
:Permission: Writer
:Parameters:

                 {

                 'name': 'value'

                 }

:Response: New Testsuite Subsystem
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "name": "subsystem"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def new_subsystem():
        url = ('{server_add}/api/{project}/testsuite_subsystem/').format(server_add=SERVER, project='Media')
        payload = {'name':"subsystem_name"}
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Suite Subsystem Detail
------------------------------------

We can get, update and delete a subsystem with given id.

:Object: TestsuiteSubsystem
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testsuite subsystem by id
:Usage: GET /api/(project_name)/testsuite_subsystem/(id)/
:Permission: Reader
:Parameters: None
:Response: Testsuite Subsystem Object
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 14,
        "name": "subsystem"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_subsystem():
        url = ('{server_add}/api/{project}/testsuite_subsystem/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`PUT`

:Function: Update testsuite subsystem by id
:Usage: PUT /api/(project_name)/testsuite_subsystem/(id)/
:Permission: Writer
:Parameters:

             {

             'name': 'value'

             }

:Response: Testsuite Subsystem Object
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "id": 14,
        "name": "subsystem_new"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_subsystem():
        url = ('{server_add}/api/{project}/testsuite_subsystem/(id)/').format(server_add=SERVER, project='Media')
        payload = {'name':"subsystem_new"}
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`DELETE`

:Function: Delete testsuite subsystem by id
:Usage: DELETE /api/{project}/testsuite_subsystem/(id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

 Subsystem with given id has been removed successfully.
