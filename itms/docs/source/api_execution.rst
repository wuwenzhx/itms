Test Execution
======================

This section introduces execution and its attribute.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Execution List
-----------------------

We can get test execution list by GET method and create execution by POST method.


:Object: TestExecution
:Authorization: Basic Authorization

:method:`GET`

:Function: Get execution list
:Usage: GET /api/(project_name)/testexecution/
:Permission: Reader
:Parameters: None
:Response: Execution List
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 107,
            "name": "test_undated",
            "os": 3,
            "platform": 3,
            "testplan": 79,
            "time": "2015-09-07T05:46:11Z",
            "runner": "api",
            "performance": false,
            "app": null
        },
        {
            "id": 110,
            "name": "exe_perf_1",
            "os": 3,
            "platform": 3,
            "testplan": 80,
            "time": "2015-09-21T08:10:40Z",
            "runner": "api",
            "performance": true,
            "app": 1
        },
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_execution_list():
        url = ('{server_add}/api/{project}/testexecution/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`POST`

:Function: Create new execution
:Usage: POST /api/{project}/testexecution/
:Permission: Writer
:Parameters:

           {

           "name": "value",

           "os": "value",

           "platform": "value",

           "testplan": "value",

           "runner": "value"

           }

:Response: New execution
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "name": "execution",
        "os": 3,
        "platform": 3,
        "testplan": 125,
        "runner": "api"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def new_execution():
        url = ('{server_add}/api/{project}/testexecution/').format(server_add=SERVER, project='Media')
        payload = {'name':"execution", 'os':3, 'platform':3, 'testplan':125, 'runner':"api"}
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


.. note:: Execution performance settings inherit from testplan performance settings.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Execution Detail
---------------------------

An execution cannot be updated, we can get and delete an execution with given id.

:Object: TestExecution
:Authorization: Basic Authorization

:method:`GET`

:Function: Get test execution by id
:Usage: GET /api/(project_name)/testexecution/(id)/
:Permission: Reader
:Parameters: None
:Response: TestExecution
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 210,
        "name": "execution",
        "os": 3,
        "platform": 3,
        "testplan": 125,
        "time": "2015-11-17T05:43:21Z",
        "runner": "api",
        "performance": false,
        "app": null
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_execution():
        url = ('{server_add}/api/{project}/testexecution/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`DELETE`

:Function: Delete test execution
:Usage: DELETE /api/{project}/testexecution/(id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

 Test execution with given id has been removed successfully.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Execution OS List
--------------------------

We can get execution OS list by GET method and create OS by POST method.

:Object: TestExecutionOS
:Authorization: Basic Authorization

:method:`GET`

:Function: Get test execution OS list
:Usage: GET /api/(project_name)/testexecution_os/
:Permission: Reader
:Parameters: None
:Response: Execution OS List
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 2,
            "name": "windows 10"
        },
        {
            "id": 3,
            "name": "windows 8"
        },
        {
            "id": 4,
            "name": "ubuntu"
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_executionOS_list():
        url = ('{server_add}/api/{project}/testexecution_os/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`POST`

:Function: Create new test execution OS
:Usage: POST /api/{project}/testexecution_os/
:Permission: Writer
:Parameters:

        {

        'name': 'value'

        }

:Response: New test execution os
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "name": "ubuntu14.04"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def new_executionOS():
        url = ('{server_add}/api/{project}/testexecution_os/').format(server_add=SERVER, project='Media')
        payload = {'name':"ubuntu14.04"}
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Execution OS Detail
-------------------------------

We can get, update and delete an execution OS with given id.

:Object: TestExecutionOS
:Authorization: Basic Authorization

:method:`GET`

:Function: Get execution os by id
:Usage: GET /api/(project_name)/testexecution_os/(os_id)/
:Permission: Reader
:Parameters: None
:Response: Test execution os Object
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 7,
        "name": "ubuntu14.04"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_executionOS():
        url = ('{server_add}/api/{project}/testexecution_os/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

:method:`PUT`

:Function: Update execution os by id
:Usage: PUT /api/(project_name)/testexecution_os/(os_id)/
:Permission: Writer
:Parameters:

        {

        'name': 'value'

        }

:Response: Test execution os Object
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "id": 7,
        "name": "ubuntu14.04_new"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_executionOS():
        url = ('{server_add}/api/{project}/testexecution_os/(id)/').format(server_add=SERVER, project='Media')
        payload = {'name':"ubuntu14.04_new"}
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

:method:`DELETE`

:Function: Delete execution os by id
:Usage: DELETE /api/(project_name)/testexecution_os/(os_id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

 Execution OS with given id has been removed successfully.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Execution Platform
----------------------------

We can get execution platform list by GET method and create platform by POST method.

:Object: TestExecutionPlatform
:Authorization: Basic Authorization

:method:`GET`

:Function: Get test execution platform list
:Usage: GET /api/(project_name)/testexecution_platform/
:Permission: Reader
:Parameters: None
:Response: Execution platform List
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 3,
            "name": "platform_3"
        },
        {
            "id": 4,
            "name": "platform_2"
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_platform_list():
        url = ('{server_add}/api/{project}/testexecution_platform/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`POST`

:Function: Create new test execution platform
:Usage: POST /api/{project}/testexecution_platform/
:Permission: Writer
:Parameters:

        {

        'name': 'value'

        }

:Response: New test execution platform
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "name": "platform"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def new_platform():
        url = ('{server_add}/api/{project}/testexecution_platform/').format(server_add=SERVER, project='Media')
        payload = {'name':"platform"}
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Execution Platform Detail
-----------------------------------

We can get, update and delete a platform with given id.


:Object: TestExecutionPlatform
:Authorization: Basic Authorization

:method:`GET`

:Function: Get execution platform by id
:Usage: GET /api/(project_name)/testexecution_platform/(platform_id)/
:Permission: Reader
:Parameters: None
:Response: Test execution platform Object
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 6,
        "name": "platform"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_platform():
        url = ('{server_add}/api/{project}/testexecution_platform/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`PUT`

:Function: Update execution os by id
:Usage: PUT /api/{project}/testexecution_platform/(id)/
:Permission: Writer
:Parameters:

        {

        'name': 'value'

        }

:Response: Test execution platform Object
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "id": 6,
        "name": "platform_new"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_platform():
        url = ('{server_add}/api/{project}/testexecution_platform/(id)/').format(server_add=SERVER, project='Media')
        payload = {'name':"platform_new"}
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

:method:`DELETE`

:Function: Delete execution os by id
:Usage: DELETE /api/{project}/testexecution_platform/(id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

 Test execution platform with given id has been removed successfully.