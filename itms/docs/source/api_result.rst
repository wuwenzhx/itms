Test Result
=================

This section introduces test result elements.

If you want to do operations on DPDK test result elements, please start from - :ref:`api-dpdk`.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Execution Suite Result
------------------------------

We can get suite result list by GET method with given execution id.

:Object: TestExecutionSuiteResult
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testsuite result by execution id
:Usage: GET /api/(project_name)/testexecution_suite_result/(execution_id)/
:Permission: Reader
:Parameters: None
:Response: Testsuite result list
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    [
        {
            "id": 692,
            "testexecution": 207,
            "testsuite": 118,
            "passed": 3,
            "failed": 3,
            "block": 3,
            "na": 3,
            "total": 16,
            "time": "2015-11-13T13:24:27Z"
        },
        {
            "id": 693,
            "testexecution": 207,
            "testsuite": 119,
            "passed": 3,
            "failed": 3,
            "block": 3,
            "na": 3,
            "total": 24,
            "time": "2015-11-13T13:24:27Z"
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_exe_suite_result():
        url = ('{server_add}/api/{project}/testexecution_suite_result/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Testsuite Testcase
--------------------------

Testsuite has related Testcase, we can get Testcase list by GET method with given Testsuite id.


:Object: TestsuiteTestcase
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testcase list by testsuite id
:Usage: GET /api/(project_name)/testsuite_testcase/(suite_id)/
:Permission: Reader
:Parameters: None
:Response: Testcase list
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    [
        {
            "id": 91,
            "name": "case_91",
            "type": 20,
            "description": "xxxx",
            "script_path": "xxxx",
            "config_path": "xxxx",
            "parameters": "xxxx",
            "feature": 29,
            "testsuite": [
                112,
                118,
                119
            ],
            "performance": false,
            "app": null,
            "del_flag": false
        },
        {
            "id": 92,
            "name": "case_92",
            "type": 20,
            "description": null,
            "script_path": null,
            "config_path": null,
            "parameters": null,
            "feature": null,
            "testsuite": [
                112,
                118,
                119
            ],
            "performance": false,
            "app": null,
            "del_flag": false
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_suite_case():
        url = ('{server_add}/api/{project}/testsuite_testcase/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suite Result Testcase Result
---------------------------------

We can get Testcase result list by GET method with given its related Testsuite result id.

:Object: SuiteresultTestcaseResult
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testcase result by testsuite result id
:Usage: GET /api/(project_name)/suiteresult_caseresult/(suiteresult_id)/
:Permission: Reader
:Parameters: None
:Response: Testcase result list
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    [
        {
            "id": 1560,
            "testcase": 91,
            "testsuite_result": 692,
            "result": "n/a",
            "bug": "1.5.1 bug",
            "log": "1.5.1 log",
            "comments": "1.5.1 test"
        },
        {
            "id": 1561,
            "testcase": 92,
            "testsuite_result": 692,
            "result": "norun",
            "bug": "1.5.1 bug",
            "log": "1.5.1 log",
            "comments": "1.5.1 test"
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_suiteresult_caseresult():
        url = ('{server_add}/api/{project}/suiteresult_caseresult/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Testcase Result List
-----------------------------------

We can get Testcase result list by GET method.

:Object: TestcaseResult
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testcase result list
:Usage: GET /api/(project_name)/testcase_result/
:Permission: Reader
:Parameters: None
:Response: Testcase result list
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 1585,
            "testcase": 39,
            "testsuite_result": 693,
            "result": "norun",
            "bug": "1.5.1 bug",
            "log": "1.5.1 log",
            "comments": "1.5.1 test"
        },
        {
            "id": 1586,
            "testcase": 17,
            "testsuite_result": 694,
            "result": "pass",
            "bug": "1.5.1 bug",
            "log": "1.5.1 log",
            "comments": "1.5.1 test"
        },
        {
            "id": 1589,
            "testcase": 22,
            "testsuite_result": 694,
            "result": "fail",
            "bug": "1.5.1 bug",
            "log": "1.5.1 log",
            "comments": "1.5.1 test"
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_case_result_list():
        url = ('{server_add}/api/{project}/testcase_result/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Testcase Result Detail
--------------------------

We can get and update a Testcase result by GET and PUT method.


:Object: TestcaseResult
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testcase result by id
:Usage: GET /api/(project_name)/testcase_result/(testcaseresult_id)/
:Permission: Reader
:Parameters: None
:Response: Testcase result
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 1599,
        "testcase": 90,
        "testsuite_result": 694,
        "result": "n/a",
        "bug": "1.5.1 bug",
        "log": "1.5.1 log",
        "comments": "1.5.1 test"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_case_result():
        url = ('{server_add}/api/{project}/testcase_result/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`PUT`

:Function: Update testcase result by id
:Usage: PUT /api/(project_name)/testcase_result/(testcaseresult_id)/
:Permission: Writer
:Parameters:

           {

           'testcase': 'value',

           'testsuite_result': 'value',

           'result': 'value',

           'bug': 'value',

           'log': 'value',

           'comments': 'value'

           }

:Response: Testcase result
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "id": 1590,
        "testcase": 23,
        "testsuite_result": 694,
        "result": "pass",
        "bug": "1.5.1 bug_new",
        "log": "1.5.1 log_new",
        "comments": "1.5.1 test_new"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_case_result():
        url = ('{server_add}/api/{project}/testcase_result/(id)/').format(server_add=SERVER, project='Media')
        payload = {'testcase':23, 'testsuite_result':694, 'result': "fail", 'bug':"1.5.1 bug", 'log':"1.5.1 log",
                   'comments':"1.5.1 test"}
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


.. note:: Cannot update testcase and testsuite_result.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Perf Testsuite Result
---------------------------------

We can get a performance Testsuite result by GET method.


:Object: PerfTestSuiteResult
:Authorization: Basic Authorization

:method:`GET`

:Function: Get Testexecution Perf Suite Result by id
:Usage: GET api/(project_name)/testexecution_perf_suite_result/(perftestexecution_id)
:Permission: Reader
:Parameters: None
:Response: testexecution perf suite result
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    [
        {
            "id": 146,
            "testexecution": 158,
            "testsuite": 94,
            "app": 1
        },
        {
            "id": 147,
            "testexecution": 158,
            "testsuite": 95,
            "app": 1
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_perf_testsuite_result():
        url = ('{server_add}/api/{project}/testexecution_perf_suite_result/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Perf Testcase Result List
----------------------------------

We can get performance Testcase result list by GET method.


:Object: PerfTestCaseResult
:Authorization: Basic Authorization

:method:`GET`

:Function: Get perf testcase result list
:Usage: GET /api/(project_name)/perf_testcase_result/
:Permission: Reader
:Parameters: None
:Response: perf testcase result list
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 717,
            "testcase": 173,
            "perf_testsuite_result": 265,
            "bug": "1.5.1 perf bug",
            "log": "1.5.1 perf log",
            "comments": "1.5.1 perf comments"
        },
        {
            "id": 718,
            "testcase": 178,
            "perf_testsuite_result": 265,
            "bug": "1.5.1 perf bug",
            "log": "1.5.1 perf log",
            "comments": "1.5.1 perf comments"
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_perf_testcase_result_list():
        url = ('{server_add}/api/{project}/perf_testcase_result/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Perf Testcase Result Detail
------------------------------------

We can get and update a Testcase result by GET and PUT method.


:Object: PerfTestCaseResult
:Authorization: Basic Authorization

:method:`GET`

:Function: Get perf testcase result by id
:Usage: GET /api/(project_name)/perf_testcase_result/(perftestcaseresult_id)/
:Permission: Reader
:Parameters: None
:Response: perf testcase result
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 1,
        "testcase": 1185,
        "perf_testsuite_result": 1,
        "bug": "",
        "log": "log:100",
        "comments": "comments:100"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_perf_testcase_result():
        url = ('{server_add}/api/{project}/perf_testcase_result/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`PUT`

:Function: Update perf testcase result by id
:Usage: PUT /api/(project_name)/perf_testcase_result/(perftestcaseresult_id)/
:Permission: Writer
:Parameters:

        {

        'testcase': 'value',

        'perf_testsuite_result': 'value',

        'bug': 'value',

        'log': 'value',

        'comments': 'value'

        }

:Response: perf testcase result
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "testcase": 1185,
        "perf_testsuite_result": 1,
        "bug": "100",
        "log": "log:100 new",
        "comments": "comments:100 new"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_perf_testcase_result():
        url = ('{server_add}/api/{project}/perf_testcase_result/(id)/').format(server_add=SERVER, project='Media')
        payload = {'testcase':1185, 'perf_testsuite_result':1, 'bug':"100", 'log':"log:100 new",
                  'comments':"comments:100 new"}
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Perf Testcase Result Detail List
-----------------------------------

We can get performance Testcase result detail list by GET method and create a result detail by POST method.

:Object: PerfTestCaseResultDetail
:Authorization: Basic Authorization

:method:`GET`

:Function: Get perf testcase result detail list
:Usage: GET /api/(project_name)/perf_testcase_result_detail/
:Permission: Reader
:Parameters: None
:Response: perf testcase result detail list
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 1,
            "perf_testcase_result": 1,
            "key": 7,
            "value": 15.0,
            "app": 2
        },
        {
            "id": 2,
            "perf_testcase_result": 2,
            "key": 2,
            "value": 97.0,
            "app": 2
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_perf_testcase_result_detail_list():
        url = ('{server_add}/api/{project}/perf_testcase_result_detail/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

:method:`POST`

:Function: Create new perf testcase result detail
:Usage: POST /api/{project}/perf_testcase_result_detail/
:Permission: Writer
:Parameters:

                {

                  'perf_testsuite_result': 'value',

                  'key': 'value',

                  'value': 'value',

                  'app': 'value'

                }

:Response: New perf testcase result detail
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "perf_testcase_result": 96,
        "key": 7,
        "value": 80,
        "app": 2
    }

:Python Code:

.. code-block:: python
    :linenos:

    def new_perf_testcase_result_detail():
        url = ('{server_add}/api/{project}/perf_testcase_result_detail/').format(server_add=SERVER, project='Media')
        payload = {'perf_testcase_result':96, 'key':7, 'value':80, 'app':2 }
        r = requests.post(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Perf Testcase Result Detail PK
-----------------------------------

We can get and update perf Testcase result detail by GET and PUT method with given result detail id.

:Object: PerfTestCaseResultDetail
:Authorization: Basic Authorization

:method:`GET`

:Function: Get perf testcase result detail by id
:Usage: GET /api/(project_name)/perf_testcase_result/(perftestcaseresultdetail_id)/
:Permission: Reader
:Parameters: None
:Response: perf testcase result detail
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 525,
        "perf_testcase_result": 139,
        "key": 4,
        "value": 29.32,
        "app": 1
    }


:Python Code:

.. code-block:: python
    :linenos:

    def get_perf_testcase_result_detail():
        url = ('{server_add}/api/{project}/perf_testcase_result_detail/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`PUT`

:Function: Update perf testcase result detail by id
:Usage: PUT /api/(project_name)/perf_testcase_result/(perftestcaseresultdetail_id)/
:Permission: Writer
:Parameters:

                {

                  'perf_testsuite_result': 'value',

                  'key': 'value',

                  'value': 'value',

                  'app': 'value'

                }

:Response: perf testcase result detail
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "perf_testcase_result": 139,
        "key": 1,
        "value": 23,
        "app": 1
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_perf_testcase_result_detail():
        url = ('{server_add}/api/{project}/perf_testcase_result_detail/(id)/').format(server_add=SERVER, project='Media')
        payload = {'perf_testcase_result':139, 'key':2, 'value': 29.222, 'app':1 }
        r = requests.put(url, payload, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Perf Testsuite Result Testcase Result List
--------------------------------------------------

We can get performance Testcase result by GET method with given Testsuite result id.

:Object: PerfTestSuiteResultTestCaseResult
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testcase result by perf testsuite result id
:Usage: GET /api/(project_name)/perf_suiteresult_caseresult/(perftestsuiteresult_id)/
:Permission: Reader
:Parameters: None
:Response: Perf testcase result list
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    [
        {
            "id": 714,
            "testcase": 177,
            "perf_testsuite_result": 265,
            "bug": "1.5.1 perf bug",
            "log": "1.5.1 perf log",
            "comments": "1.5.1 perf comments"
        },
        {
            "id": 715,
            "testcase": 176,
            "perf_testsuite_result": 265,
            "bug": "1.5.1 perf bug",
            "log": "1.5.1 perf log",
            "comments": "1.5.1 perf comments"
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_perf_testcaseresult_by_suiteresultid():
        url = ('{server_add}/api/{project}/perf_suiteresult_caseresult/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Perf Testcase Result Testcase Detail
-------------------------------------------

We can get performance Testcase result detail by GET method with given Testcase result id.

:Object: PerfTestcaseResultTestcaseDetailResult
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testcase detail result by perf testcase result id
:Usage: GET /api/(project_name)/perf_caseresult_detailresult/(perftestcaseresult_id)/
:Permission: Reader
:Parameters: None
:Response: Perf testcase detail result list
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    [
        {
            "id": 370,
            "perf_testcase_result": 120,
            "key": 1,
            "value": 29.32,
            "app": 1
        },
        {
            "id": 371,
            "perf_testcase_result": 120,
            "key": 2,
            "value": 29.32,
            "app": 1
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_perf_testcasedetailresult_by_caseresultid():
        url = ('{server_add}/api/{project}/perf_caseresult_detailresult/(id)/').format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print '==========='
        print r
        print '==========='
        print r.json()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. role:: dpdk

.. note:: Following elements only for DPDK performance test.

.. _api-dpdk:

:dpdk:`DPDK` Perf Testsuite Result Testcasce Result List
------------------------------------------------------------

We can get DPDK performance Testcase result by GET method with given Testsuite result id.


:Object: PerfDPDKTestSuiteResultTestCaseResult
:Authorization: Basic Authorization

:method:`GET`

:Function: Get testcase result by perf testsuite result id
:Usage: GET /api/(project_name)/perf_dpdk_suiteresult_caseresult/(perftestsuiteresult_id)/
:Permission: Reader
:Parameters: None
:Response: Perf dpdk testcase result list
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    [
        {
            "id": 323,
            "testcase": 1207,
            "perf_testsuite_result": 176,
            "bug": null,
            "log": null,
            "comments": null
        },
        {
            "id": 324,
            "testcase": 1206,
            "perf_testsuite_result": 176,
            "bug": null,
            "log": null,
            "comments": null
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_perf_dpdk_testcaseresult_by_suiteresultid():
        url = ('{server_add}/api/{project}/perf_dpdk_suiteresult_caseresult/(id)/').format(server_add=SERVER, project='DPDK')
        r = requests.get(url, auth=HTTPBasicAuth(username, password))
        print '===================='
        print r
        print '===================='
        print r.json()
        return r.json()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. role:: dpdk

:dpdk:`DPDK` Perf Testcase Result Testcase Detail
----------------------------------------------------

We can get DPDK performance Testcase result detail by GET method with given DPDK Testcase result id.

:Object: PerfDPDKTestcaseResultTestcaseDetailResult
:Authorization: Basic Authorization

:method:`GET`

:Function: Get dpdk testcase detail result by perf dpdk testcase result id
:Usage: GET /api/(project_name)/perf_dpdk_caseresult_detailresult/(perfdpdktestcaseresult_id)/
:Permission: Reader
:Parameters: None
:Response: Perf dpdk testcase detail result list
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    [
        {
            "id": 1,
            "perf_dpdk_testcase_result": 4,
            "key": 12,
            "value": "128",
            "app": 5,
            "group": 1
        },
        {
            "id": 2,
            "perf_dpdk_testcase_result": 4,
            "key": 13,
            "value": "20",
            "app": 5,
            "group": 1
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_perf_dpdk_testcasedetailresult_by_caseresultid():
        url = ('{server_add}/api/{project}/perf_dpdk_caseresult_detailresult/(id)/').format(server_add=SERVER, project='DPDK')
        r = requests.get(url, auth=HTTPBasicAuth(username, password))
        print '==========='
        print r
        print '==========='
        print r.json()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. role:: dpdk

:dpdk:`DPDK` Perf Testcase Result
-----------------------------------

We can get and update a DPDK perf testcase result by given a DPDK perf testcase result detail id.

:Object: PerfDPDKTestCaseResult
:Authorization: Basic Authorization

:method:`GET`

:Function: Get perf dpdk testcase result by perf dpdk testcase result detail id
:Usage: GET /api/(project_name)/perf_dpdk_testcase_result/(perfdpdktestcaseresultdetail_id)/
:Permission: Reader
:Parameters: None
:Response: perf dpdk testcase result
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 4,
        "testcase": 1207,
        "perf_testsuite_result": 54,
        "bug": "test",
        "log": "test log",
        "comments": "test comments"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_perf_dpdk_testcaseresult_by_caseresultdetailid():
        url = ('{server_add}/api/{project}/perf_dpdk_testcase_result/(id)/').format(server_add=SERVER, project='DPDK')
        r = requests.get(url, auth=HTTPBasicAuth(username, password))
        print '==========='
        print r
        print '==========='
        print r.json()


:method:`PUT`

:Function: Update perf dpdk testcase result detail by perf dpdk testcase result detail id
:Usage: PUT /api/(project_name)/perf_dpdk_testcase_result/(perfdpdktestcaseresultdetail_id)/
:Permission: Writer
:Parameters:

                {

                  'testcase': 'value',

                  'perf_testsuite_result': 'value',

                  'bug': 'value',

                  'log': 'value',

                  'comments': 'value'

                }

:Response: perf dpdk testcase result detail
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "id": 4,
        "testcase": 1207,
        "perf_testsuite_result": 54,
        "bug": "test_new",
        "log": "test log new",
        "comments": "test comments new"
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_perf_dpdk_testcaseresult_by_caseresultdetailid():
        url = ('{server_add}/api/{project}/perf_dpdk_testcase_result/(id)/').format(server_add=SERVER, project='DPDK')
        payload = {'testcase': 1207, 'perf_testsuite_result': 54, 'bug': "test", 'log': "log", 'comments': "comment"}
        r = requests.put(url, payload, auth=HTTPBasicAuth(username, password))
        print '===================='
        print r
        print '===================='
        print r.json()
        return r.json()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. role:: dpdk

:dpdk:`DPDK` Perf Testcase Result Detail List
----------------------------------------------

We can get DPDK performance testcase result detail list by GET method and create Testplan by POST method.

:Object: PerfDPDKTestCaseResultDetail
:Authorization: Basic Authorization

:method:`GET`

:Function: Get perf dpdk testcase result detail list
:Usage: GET /api/(project_name)/perf_dpdk_testcase_result_detail/
:Permission: Reader
:Parameters: None
:Response: perf dpdk testcase result detail list
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 11522,
            "perf_dpdk_testcase_result": 337,
            "key": 12,
            "value": "1518",
            "app": 5,
            "group": 7
        },
        {
            "id": 11523,
            "perf_dpdk_testcase_result": 337,
            "key": 13,
            "value": "31",
            "app": 5,
            "group": 7
        }
    ]

:Python Code:

.. code-block:: python
    :linenos:

    def get_perf_dpdk_case_detail_list():
        url = ('{server_add}/api/{project}/perf_dpdk_testcase_result_detail/').format(server_add=SERVER, project='DPDK')
        r = requests.get(url, auth=HTTPBasicAuth(username, password))
        print '===================='
        print r
        print '===================='
        print r.json()
        return r.json()


:method:`POST`

:Function: Create new perf dpdk testcase result detail
:Usage: POST /api/(project_name)/perf_dpdk_testcase_result_detail/
:Permission: Writer
:Parameters:

                {

                  'perf_dpdk_testcase_result': 'value',

                  'key': 'value',

                  'value': 'value',

                  'app': 'value',

                  'group': 'value'

                }

:Response: New perf dpdk testcase result detail
:Successful Status: HTTP_201_CREATED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
:Sample Input:

::

    {
        "perf_dpdk_testcase_result": 4,
        "key": 19,
        "value": "8E+007",
        "app": 5,
        "group": 3
    }

:Python Code:

.. code-block:: python
    :linenos:

    def new_perf_dpdk_case_detail():
        url = ('{server_add}/api/{project}/perf_dpdk_testcase_result_detail/').format(server_add=SERVER, project='DPDK')
        payload = {'perf_dpdk_testcase_result': 4, 'key': 12, 'value': 128, 'app': 5, 'group': 5}
        r = requests.post(url, payload, auth=HTTPBasicAuth(username, password))
        print '===================='
        print r
        print '===================='
        print r.json()
        return r.json()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. role:: dpdk

:dpdk:`DPDK` Perf Testcase Result Detail PK
----------------------------------------------

We can get, update and delete a DPDK performance testcase result detail with given id.


:Object: PerfDPDKTestCaseResultDetail
:Authorization: Basic Authorization

:method:`GET`

:Function: Get perf dpdk testcase result detail by id
:Usage: GET /api/(project_name)/perf_dpdk_testcase_result_detail/(perfdpdktestcaseresultdetail_id)/
:Permission: Reader
:Parameters: None
:Response: perf dpdk testcase result detail
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

    {
        "id": 1,
        "perf_dpdk_testcase_result": 4,
        "key": 12,
        "value": "64",
        "app": 5,
        "group": 1
    }

:Python Code:

.. code-block:: python
    :linenos:

    def get_perf_dpdk_case_detail():
        url = ('{server_add}/api/{project}/perf_dpdk_testcase_result_detail/(id)/').format(server_add=SERVER, project='DPDK')
        r = requests.get(url, auth=HTTPBasicAuth(username, password))
        print '===================='
        print r
        print '===================='
        print r.json()
        return r.json()


:method:`PUT`

:Function: Update perf dpdk testcase result detail by id
:Usage: PUT /api/(project_name)/perf_dpdk_testcase_result_detail/(perfdpdktestcaseresultdetail_id)/
:Permission: Writer
:Parameters:

               {

                  'perf_dpdk_testcase_result': 'value',

                  'key': 'value',

                  'value': 'value',

                  'app': 'value',

                  'group': 'value'

                }

:Response: perf dpdk testcase result detail
:Successful Status: HTTP_202_ACCEPTED
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
:Sample Input:

::

    {
        "perf_dpdk_testcase_result": 6,
        "key": 14,
        "value": "46",
        "app": 1,
        "group": 8
    }

:Python Code:

.. code-block:: python
    :linenos:

    def update_perf_dpdk_case_detail():
        url = ('{server_add}/api/{project}/perf_dpdk_testcase_result_detail/(id)/').format(server_add=SERVER, project='DPDK')
        payload = {'perf_dpdk_testcase_result': 4, 'key': 12, 'value': 128, 'app': 5, 'group': 1}
        r = requests.put(url, payload, auth=HTTPBasicAuth(username, password))
        print '===================='
        print r
        print '===================='
        print r.json()
        return r.json()

:method:`DELETE`

:Function: Delete perf dpdk testcase result detail by id
:Usage: DELETE /api/(project_name)/perf_dpdk_testcase_result_detail/(perfdpdktestcaseresultdetail_id)/
:Permission: Writer
:Parameters: None
:Response: None
:Successful Status: HTTP_204_NO_CONTENT
:Unsuccessful Status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
:Sample Output:

::

  Perf dpdk testcase result detail with given id has been removed successfully.