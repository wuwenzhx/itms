====================================
Object: Project
url: http://server_url/api/project
Authorization: Basic Authorization

Function: Get all of project list
    Method: GET
    Permission: All
    parameters: None
    response: Project List
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

====================================
Object: RequirementType
url: http://server_url/api/(project_name)/requirement_type/
Authorization: Basic Authorization

Function: Get requirement type list
    Method: GET
    Permission: Reader
    parameters: None
    response: Requirement Type List
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new requirement type
    Method: POST
    Permission: Writer
    parameters: {'name': 'value'}
    response: New Requirement Type
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: RequirementType
url: http://server_url/api/(project_name)/requirement_type/(id)/
Authorization: Basic Authorization

Function: Get requirement type by id
    Method: GET
    Permission: Reader
    parameters: None
    response: Requirement Type Object
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update requirement type by id
    Method: PUT
    Permission: Writer
    parameters: {'name': 'value'}
    response: Requirement Type Object
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,
                         HTTP_404_NOT_FOUND

Function: Delete requirement type by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: Requirement
url: http://server_url/api/(project_name)/requirement/
Authorization: Basic Authorization

Function: Get requirement list
    Method: GET
    Permission: Reader
    parameters: None
    response: Requirement List
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new requirement
    Method: POST
    Permission: Writer
    parameters: {
                'name': 'value',
                'owner': 'value',
                'type': 'value',
                'description': 'value'
    }
    response: New Requirement
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: Requirement
url: http://server_url/api/(project_name)/requirement/(id)/
Authorization: Basic Authorization

Function: Get requirement by id
    Method: GET
    Permission: Reader
    parameters: None
    response: Requirement Object
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update requirement by id
    Method: PUT
    Permission: Writer
    parameters: {
                'name': 'value',
                'owner': 'value',
                'type': 'value',
                'description': 'value'
    }
    response: Requirement Object
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,
                         HTTP_404_NOT_FOUND

Function: Delete requirement by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: FeatureComponent
url: http://server_url/api/(project_name)/feature_component/
Authorization: Basic Authorization

Function: Get feature component list
    Method: GET
    Permission: Reader
    parameters: None
    response: Feature Component List
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new feature component
    Method: POST
    Permission: Writer
    parameters: {'name': 'value'}
    response: New Feature Component
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: FeatureComponent
url: http://server_url/api/(project_name)/feature_component/(id)/
Authorization: Basic Authorization

Function: Get feature component by id
    Method: GET
    Permission: Reader
    parameters: None
    response: Feature Component Object
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update feature component by id
    Method: PUT
    Permission: Writer
    parameters: {'name': 'value'}
    response: Feature Component Object
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,
                         HTTP_404_NOT_FOUND

Function: Delete feature component by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: Feature
url: http://server_url/api/(project_name)/feature/
Authorization: Basic Authorization

Function: Get feature list
    Method: GET
    Permission: Reader
    parameters: None
    response: Feature List
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new feature
    Method: POST
    Permission: Writer
    parameters: {
                'name': 'value',
                'owner': 'value',
                'component': 'value',
                'requirement': 'value',
                'description': 'value'
    }
    response: New Feature
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: Feature
url: http://server_url/api/(project_name)/feature/(id)/
Authorization: Basic Authorization

Function: Get feature by id
    Method: GET
    Permission: Reader
    parameters: None
    response: Feature Object
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update feature by id
    Method: PUT
    Permission: Writer
    parameters: {
                'name': 'value',
                'owner': 'value',
                'component': 'value',
                'requirement': 'value',
                'description': 'value'
    }
    response: Feature Object
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,
                         HTTP_404_NOT_FOUND

Function: Delete feature by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: TestplanCategory
url: http://server_url/api/(project_name)/testplan_category/
Authorization: Basic Authorization

Function: Get testplan category list
    Method: GET
    Permission: Reader
    parameters: None
    response: Testplan Category List
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new testplan category
    Method: POST
    Permission: Writer
    parameters: {'name': 'value'}
    response: New Testplan Category
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: TestplanCategory
url: http://server_url/api/(project_name)/testplan_category/(id)/
Authorization: Basic Authorization

Function: Get testplan category by id
    Method: GET
    Permission: Reader
    parameters: None
    response: Testplan Category Object
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update testplan category by id
    Method: PUT
    Permission: Writer
    parameters: {'name': 'value'}
    response: Testplan Category Object
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,
                         HTTP_404_NOT_FOUND

Function: Delete testplan category by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: Testplan
url: http://server_url/api/(project_name)/testplan/
Authorization: Basic Authorization

Function: Get testplan list
    Method: GET
    Permission: Reader
    parameters: None
    response: Testplan List
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new testplan
    Method: POST
    Permission: Writer
    parameters: {
                'name': 'value',
                'category': 'value',
                'owner': 'value',
                'start_time': 'value',
                'end_time': 'value',
                'description': 'value',
                'performance': 'value',
                'app': 'value'
    }
    response: New Testplan
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: Testplan
url: http://server_url/api/(project_name)/testplan/(id)/
Authorization: Basic Authorization

Function: Get testplan by id
    Method: GET
    Permission: Reader
    parameters: None
    response: Testplan Object
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update testplan by id
    Method: PUT
    Permission: Writer
    parameters: {
                'name': 'value',
                'category': 'value',
                'owner': 'value',
                'start_time': 'value',
                'end_time': 'value',
                'description': 'value',
                'performance': 'value',
                'app': 'value'
    }
    response: Testplan Object
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,
                         HTTP_404_NOT_FOUND

Function: Delete testplan by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: TestsuiteSubsystem
url: http://server_url/api/(project_name)/testsuite_subsystem/
Authorization: Basic Authorization

Function: Get testsuite subsystem list
    Method: GET
    Permission: Reader
    parameters: None
    response: Testsuite Subsystem List
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new testsuite subsystem
    Method: POST
    Permission: Writer
    parameters: {'name': 'value'}
    response: New Testsuite Subsystem
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: TestsuiteSubsystem
url: http://server_url/api/(project_name)/testsuite_subsystem/(id)/
Authorization: Basic Authorization

Function: Get testsuite subsystem by id
    Method: GET
    Permission: Reader
    parameters: None
    response: Testsuite Subsystem Object
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update testsuite subsystem by id
    Method: PUT
    Permission: Writer
    parameters: {'name': 'value'}
    response: Testsuite Subsystem Object
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,
                         HTTP_404_NOT_FOUND

Function: Delete testsuite subsystem by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: Testsuite
url: http://server_url/api/(project_name)/testsuite/
Authorization: Basic Authorization

Function: Get testsuite list
    Method: GET
    Permission: Reader
    parameters: None
    response: Testsuite List
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new testsuite
    Method: POST
    Permission: Writer
    parameters: {
                'name': 'value',
                'subsystem': 'value',
                'testplan': 'value',
                'description': 'value',
                'performance': 'value',
                'app': 'value'
    }
    response: New Testsuite
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: Testsuite
url: http://server_url/api/(project_name)/testsuite/(id)/
Authorization: Basic Authorization

Function: Get testsuite by id
    Method: GET
    Permission: Reader
    parameters: None
    response: Testsuite Object
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update testsuite by id
    Method: PUT
    Permission: Writer
    parameters: {
                'name': 'value',
                'subsystem': 'value',
                'testplan': 'value',
                'description': 'value',
                'performance': 'value',
                'app': 'value'
    }
    response: Testsuite Object
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,
                         HTTP_404_NOT_FOUND

Function: Delete testsuite by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

====================================
Object: TestcaseType
url: http://server_url/api/(project_name)/testcase_type/
Authorization: Basic Authorization

Function: Get testcase type list
    Method: GET
    Permission: Reader
    parameters: None
    response: Testcase Type List
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new testcase type
    Method: POST
    Permission: Writer
    parameters: {'name': 'value'}
    response: New Testcase Type
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: TestcaseType
url: http://server_url/api/(project_name)/testcase_type/(id)/
Authorization: Basic Authorization

Function: Get testcase type by id
    Method: GET
    Permission: Reader
    parameters: None
    response: Testcase Type Object
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update testcase type by id
    Method: PUT
    Permission: Writer
    parameters: {'name': 'value'}
    response: Testcase Type Object
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,
                         HTTP_404_NOT_FOUND

Function: Delete testcase type by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: Testcase
url: http://server_url/api/(project_name)/testcase/
Authorization: Basic Authorization

Function: Get testcase list
    Method: GET
    Permission: Reader
    parameters: None
    response: Testcase List
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new testcase
    Method: POST
    Permission: Writer
    parameters: {
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
    response: New Testcase
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: Testcase
url: http://server_url/api/(project_name)/testcase/(id)/
Authorization: Basic Authorization

Function: Get testcase by id
    Method: GET
    Permission: Reader
    parameters: None
    response: Testcase Object
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update testcase by id
    Method: PUT
    Permission: Writer
    parameters: {
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
    response: Testcase Object
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,
                         HTTP_404_NOT_FOUND

Function: Delete testcase by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

====================================
Object: TestExecutionOS
url: http://server_url/api/(project_name)/testexecution_os/
Authorization: Basic Authorization

Function: Get test execution OS list
    Method: GET
    Permission: Reader
    parameters: None
    response: Execution OS List
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new test execution OS
    Method: POST
    Permission: Writer
    parameters: {'name': 'value'}
    response: New test execution os
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: TestExecutionOS
url: http://server_url/api/(project_name)/testexecution_os/(os_id)/
Authorization: Basic Authorization

Function: Get execution os by id
    Method: GET
    Permission: Reader
    parameters: None
    response: Test execution os Object
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update execution os by id
    Method: PUT
    Permission: Writer
    parameters: {'name': 'value'}
    response: Test execution os Object
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,
                         HTTP_404_NOT_FOUND

Function: Delete execution os by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: TestExecutionPlatform
url: http://server_url/api/(project_name)/testexecution_platform/
Authorization: Basic Authorization

Function: Get test execution platform list
    Method: GET
    Permission: Reader
    parameters: None
    response: Execution platform List
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new test execution platform
    Method: POST
    Permission: Writer
    parameters: {'name': 'value'}
    response: New test execution platform
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: TestExecutionPlatform
url: http://server_url/api/(project_name)/testexecution_platform/(platform_id)/
Authorization: Basic Authorization

Function: Get execution platform by id
    Method: GET
    Permission: Reader
    parameters: None
    response: Test execution platform Object
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update execution os by id
    Method: PUT
    Permission: Writer
    parameters: {'name': 'value'}
    response: Test execution platform Object
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,
                         HTTP_404_NOT_FOUND

Function: Delete execution os by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: TestExecution
url: http://server_url/api/(project_name)/testexecution/
Authorization: Basic Authorization

Function: Get execution list
    Method: GET
    Permission: Reader
    parameters: None
    response: Execution List
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new execution
    Method: POST
    Permission: Writer
    parameters: {
                "name": "value",
                "os": "value",
                "platform": "value",
                "testplan": "value",
                "runner": "value"
    }
    response: New execution
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: TestExecution
url: http://server_url/api/(project_name)/testexecution/(id)/
Authorization: Basic Authorization

Function: Get test execution by id
    Method: GET
    Permission: Reader
    parameters: None
    response: TestExecution
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Delete test execution
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: TestExecutionSuiteResult
url: http://server_url/api/(project_name)/testexecution_suite_result/(execution_id)/
Authorization: Basic Authorization

Function: Get testsuite result by execution id
    Method: GET
    Permission: Reader
    parameters: None
    response: Testsuite result list
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: TestsuiteTestcase
url: http://server_url/api/(project_name)/testsuite_testcase/(suite_id)/
Authorization: Basic Authorization

Function: Get testcase list by testsuite id
    Method: GET
    Permission: Reader
    parameters: None
    response: Testcase list
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: SuiteresultTestcaseResult
url: http://server_url/api/(project_name)/suiteresult_caseresult/(suiteresult_id)/
Authorization: Basic Authorization

Function: Get testcase result by testsuite result id
    Method: GET
    Permission: Reader
    parameters: None
    response: Testcase result list
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: TestcaseResult
url: http://server_url/api/(project_name)/testcase_result/
Authorization: Basic Authorization

Function: Get testcase result list
    Method: GET
    Permission: Reader
    parameters: None
    response: Testcase result list
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

====================================
Object: TestcaseResult
url: http://server_url/api/(project_name)/testcase_result/(testcaseresult_id)/
Authorization: Basic Authorization

Function: Get testcase result by id
    Method: GET
    Permission: Reader
    parameters: None
    response: Testcase result
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update testcase result by id
    Method: PUT
    Permission: Writer
    parameters: None
    response: Testcase result
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

====================================
Object: App
url: http://server_url/api/(project_name)/app/
Authorization: Basic Authorization

Function: Get app list
    Method: GET
    Permission: Reader
    parameters: None
    response: app list
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new app
    Method: POST
    Permission: Writer
    parameters: {'name':'value'}
    response: New app 
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: App
url: http://server_url/api/(project_name)/app/(app_id)/
Authorization: Basic Authorization

Function: Get app by id
    Method: GET
    Permission: Reader
    parameters: None
    response: app
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update app by id
    Method: PUT
    Permission: Writer
    parameters: {'name': 'value'}
    response: app
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND,
                         HTTP_409_CONFLICT

Function: Delete app by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: App Attr
url: http://server_url/api/(project_name)/app_attr/
Authorization: Basic Authorization

Function: Get app attr list
    Method: GET
    Permission: Reader
    parameters: None
    response: app attr list
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new app attr
    Method: POST
    Permission: Writer
    parameters: {
                  'name':'value',
                  'app': 'value
                }
    response: New app attr 
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: App Attr
url: http://server_url/api/(project_name)/app_attr/(appattr_id)/
Authorization: Basic Authorization

Function: Get app attr by id
    Method: GET
    Permission: Reader
    parameters: None
    response: app attr
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update app attr by id
    Method: PUT
    Permission: Writer
    parameters: {
                  'name': 'value',
                  'app': 'value'
                }
    response: app attr
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND,
                         HTTP_409_CONFLICT

Function: Delete app attr by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: PerfTestSuiteResult
url: http://server_url/api/(project_name)/testexecution_perf_suite_result/(perftestexecution_id)
Authorization: Basic Authorization

Function: Get Testexecution Perf Suite Result by id
    Method: GET
    Permission: Reader
    parameters: None
    response: testexecution perf suite result 
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: PerfTestCaseResult
url: http://server_url/api/(project_name)/perf_testcase_result/
Authorization: Basic Authorization

Function: Get perf testcase result list
    Method: GET
    Permission: Reader
    parameters: None
    response: perf testcase result list
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

====================================
Object: PerfTestCaseResult
url: http://server_url/api/(project_name)/perf_testcase_result/(perftestcaseresult_id)/
Authorization: Basic Authorization

Function: Get perf testcase result by id
    Method: GET
    Permission: Reader
    parameters: None
    response: perf testcase result
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update perf testcase result by id
    Method: PUT
    Permission: Writer
    parameters: {
                  'testcase': 'value',
                  'perf_testsuite_result': 'value',
                  'bug': 'value',
                  'log': 'value',
                  'comments': 'value'
                }
    response: perf testcase result
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

====================================
Object: PerfTestCaseResultDetail
url: http://server_url/api/(project_name)/perf_testcase_result_detail/
Authorization: Basic Authorization

Function: Get perf testcase result detail list
    Method: GET
    Permission: Reader
    parameters: None
    response: perf testcase result detail list
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new perf testcase result detail
    Method: POST
    Permission: Writer
    parameters: {
                  'perf_testsuite_result': 'value',
                  'key': 'value',
                  'value': 'value',
                  'app': 'value'
                }
    response: New perf testcase result detail
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: PerfTestCaseResultDetail
url: http://server_url/api/(project_name)/perf_testcase_result_detail/(perftestcaseresultdetail_id)/
Authorization: Basic Authorization

Function: Get perf testcase result detail by id
    Method: GET
    Permission: Reader
    parameters: None
    response: perf testcase result detail
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update perf testcase result detail by id
    Method: PUT
    Permission: Writer
    parameters: {
                  'perf_testsuite_result': 'value',
                  'key': 'value',
                  'value': 'value',
                  'app': 'value'
                }
    response: perf testcase result detail
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

Function: Delete perf testcase result detail by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: PerfTestSuiteResultTestCaseResult
url: http://server_url/api/(project_name)/perf_suiteresult_caseresult/(perftestsuiteresult_id)/
Authorization: Basic Authorization

Function: Get testcase result by perf testsuite result id
    Method: GET
    Permission: Reader
    parameters: None
    response: Perf testcase result list
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: PerfTestcaseResultTestcaseDetailResult
url: http://server_url/api/(project_name)/perf_caseresult_detailresult/(perftestcaseresult_id)/
Authorization: Basic Authorization

Function: Get testcase detail result by perf testcase result id
    Method: GET
    Permission: Reader
    parameters: None
    response: Perf testcase detail result list
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: PerfDPDKTestSuiteResultTestCaseResult
url: http://server_url/api/(project_name)/perf_dpdk_suiteresult_caseresult/(perftestsuiteresult_id)/
Authorization: Basic Authorization

Function: Get testcase result by perf testsuite result id
    Method: GET
    Permission: Reader
    parameters: None
    response: Perf dpdk testcase result list
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: PerfDPDKTestcaseResultTestcaseDetailResult
url: http://server_url/api/(project_name)/perf_dpdk_caseresult_detailresult/(perfdpdktestcaseresult_id)/
Authorization: Basic Authorization

Function: Get dpdk testcase detail result by perf dpdk testcase result id
    Method: GET
    Permission: Reader
    parameters: None
    response: Perf dpdk testcase detail result list
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

====================================
Object: PerfDPDKTestCaseResult
url: http://server_url/api/(project_name)/perf_dpdk_testcase_result/(perfdpdktestcaseresultdetail_id)/
Authorization: Basic Authorization

Function: Get perf dpdk testcase result by perf dpdk testcase result detail id
    Method: GET
    Permission: Reader
    parameters: None
    response: perf dpdk testcase result
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update perf dpdk testcase result detail by perf dpdk testcase result detail id
    Method: PUT
    Permission: Writer
    parameters: {
                  'testcase': 'value',
                  'perf_testsuite_result': 'value',
                  'bug': 'value',
                  'log': 'value',
                  'comments': 'value'
                }
    response: perf dpdk testcase result detail
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

====================================
Object: PerfDPDKTestCaseResultDetail
url: http://server_url/api/(project_name)/perf_dpdk_testcase_result_detail/
Authorization: Basic Authorization

Function: Get perf dpdk testcase result detail list
    Method: GET
    Permission: Reader
    parameters: None
    response: perf dpdk testcase result detail list
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED

Function: Create new perf dpdk testcase result detail
    Method: POST
    Permission: Writer
    parameters: {
                  'perf_dpdk_testcase_result': 'value',
                  'key': 'value',
                  'value': 'value',
                  'app': 'value',
                  'group': 'value'
                }
    response: New perf dpdk testcase result detail
    successful status: HTTP_201_CREATED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

====================================
Object: PerfDPDKTestCaseResultDetail
url: http://server_url/api/(project_name)/perf_dpdk_testcase_result_detail/(perfdpdk testcaseresultdetail_id)/
Authorization: Basic Authorization

Function: Get perf dpdk testcase result detail by id
    Method: GET
    Permission: Reader
    parameters: None
    response: perf dpdk testcase result detail
    successful status: HTTP_200_OK
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

Function: Update perf dpdk testcase result detail by id
    Method: PUT
    Permission: Writer
    parameters: {
                  'perf_dpdk_testcase_result': 'value',
                  'key': 'value',
                  'value': 'value',
                  'app': 'value',
                  'group': 'value'
                }
    response: perf dpdk testcase result detail
    successful status: HTTP_202_ACCEPTED
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

Function: Delete perf dpdk testcase result detail by id
    Method: Delete
    Permission: Writer
    parameters: None
    response: None
    successful status: HTTP_204_NO_CONTENT
    unsuccessful status: HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
