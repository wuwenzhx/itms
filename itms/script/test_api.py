import requests
import json
from requests.auth import HTTPBasicAuth

IP_ADDR = 'http://127.0.0.1/api/'
SERVER = 'http://127.0.0.1'
#changed:
#username = 'xxxxxxxx'
#password = 'xxxxxxxx'
username = 'admin'
password = '1'
# 'api/project/'                                    get/new project
# 'api/requirement_type/'                           get/new requirement type
# 'api/requirement_type/(?P<pk>[0-9]+)/'            get/update specify requirement type
# 'api/requirement/'                                get/new requirement
# 'api/requirement/(?P<pk>[0-9]+)/'                 get/update specify requirement
# 'api/feature_component/'                          get/new feature component
# 'api/feature_component/(?P<pk>[0-9]+)/'           get/update specify feature component
# 'api/feature/'                                    get/new feature
# 'api/feature/(?P<pk>[0-9]+)/'                     get/update specify feature component
# 'api/testplan_category/'                          get/new testplan category
# 'api/testplan_category/(?P<pk>[0-9]+)/'           get/update specify testplan category
# 'api/testplan/'                                   get/new testplan
# 'api/testplan/(?P<pk>[0-9]+)/'                    get/update specify testplan
# 'api/testsuite_subsystem/'                        get/new testsuite subsystem
# 'api/testsuite_subsystem/(?P<pk>[0-9]+)/'         get/update specify testsuite subsystem
# 'api/testsuite/'                                  get/new testsuite
# 'api/testsuite/(?P<pk>[0-9]+)/'                   get/update specify testsuite
# 'api/testcase_type/'                              get/new testcase type
# 'api/testcase_type/(?P<pk>[0-9]+)/'               get/update specify testcase type
# 'api/testcase/'                                   get/new testcase
# 'api/testcase/(?P<pk>[0-9]+)/'                    get/update specify testcase
# 'api/testexecution_os/'                           get/new test execution os
# 'api/testexecution_os/(?P<pk>[0-9]+)/'            get/update specify test execution os
# 'api/testexecution_platform/'                     get/new test execution platform
# 'api/testexecution_platform/(?P<pk>[0-9]+)/'      get/update specify test execution platform
# 'api/testexecution/'                              get/new test execution
# 'api/testexecution_suite_result/(?P<pk>[0-9]+)/'  get specify testexecution suite result
# 'api/testsuite_testcase/(?P<pk>[0-9]+)/'          get testcase of specify testsuite
# 'api/testcase_result/'                            get/new/update testcase result for specify testsuite result


def get_project_list():
    url = IP_ADDR + 'project'
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    #r = requests.get(url)
    print r.url
    print r.status_code
    print type(r.json()), r.json()


def new_project(project_name):
    url = IP_ADDR + 'project/'
    payload = {'name': project_name}
    r = requests.post(url, payload)
    print r.url
    print r.status_code


def get_requirement_type_list():
    url = IP_ADDR + 'requirement_type'
    r = requests.get(url)
    print r.url
    print r.status_code
    print r.json()


def update_requirement_type(id, name, project):
    url = IP_ADDR + 'requirement_type/%s/' % id
    payload = {'name': name, 'project': project}
    r = requests.put(url, payload)
    print r.url
    print r.status_code
    print r.json()


def get_testplan_list():
    url = IP_ADDR + 'dpdk/testplan'
    #r = requests.get(url)
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.status_code
    print r.json()

########## I defined: ######################
#def new_dpdk_testplan(plan_id,plan_name,category_id,performance,app_id,owner,create_time,start_time,end_time,description):
def new_dpdk_testplan():
    url = '{server_add}/api/{project}/testplan/'.format(server_add=SERVER,project='dpdk') 
    payload={'id':2,'name':"plan_name","category":1,'performance':True,'app':1,'owner':"admin",'create_time':"2016-10-24T17:39:17Z",'start_time':"2016-10-24T17:39:17Z",'end_time':"2016-10-24T17:39:17Z",'description':"test"}
    r = requests.post(url, payload, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.json()
    if 201 == r.status_code:
        execution = json.loads(r.text)
        return execution['id']
    else:
        return None


#def new_dpdk_testresult(result_id,exe_id,suit_id,pass_num,fail_num,block_num,na_num,total,create_time):
def new_dpdk_testresult():
    url = '{server_add}/api/dpdk/testexecution_suite_result/1/'.format(server_add=SERVER,project='dpdk') 
    #payload={'id':2 ,'name':"dpdk2",'category':1,'performance':True,'app':1,'owner':"admin",'create_time':"2016-10-24T17:39:17Z",'start_time':"2016-10-24T17:39:17Z",'end_time':"2016-10-24T17:39:17Z",'description':"null"}
    payload={'id':1,'testexecution':2,'testsuite':1,'passed':12,'failed':21,'block':1,'na':1,'total':14}#'time':"2016-10-24T17:39:17Z",}
    #payload={'id':result_id,'testexecution':exe_id,'testsuite':suit_id,'passed':pass_num,'failed':failpnum,'block':block_num,'na':na_num,'total':total,'time':"create_time"}
    r = requests.post(url, payload, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.json()
    if 201 == r.status_code:
        execution = json.loads(r.text)
        return execution['id']
    else:
        return None


def create_execution(plan_id, name, os, platform, runner, project, performance, app):
    url = '{server_add}/api/{project}/testexecution/'.format(server_add=SERVER,
            project='dpdk')
    payload = {'name': name, 'os': os, 'platform': platform, 'testplan': plan_id,
               'runner': runner, 'project': project, 'performance': performance, 'app': app}
    r = requests.post(url, payload, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.json()
    if 201 == r.status_code:
        execution = json.loads(r.text)
        return execution['id']
    else:
        return None

#####################################################
def get_suite_result(execution_id):
    url = ('{server_add}/api/{project}/testexecution_suite_result/%s/' % execution_id).format(server_add=SERVER, project='Media')
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    print '==========='
    print r
    print '==========='
    print r.json()
    return r.json()


def get_perf_case_result(suite_reuslt_id):
    url = ('{server_add}/api/{project}/perf_suiteresult_caseresult/%s/' % suite_reuslt_id).format(server_add=SERVER, project='Media')
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    print r.json()
    return r.json()


def get_case_result(suite_result_id):
    url = ('{server_add}/api/{project}/suiteresult_caseresult/%s/' % suite_result_id).format(server_add=SERVER, project='Media')
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    return r.json()


def save_case_result(case_result_obj):
    url = ('{server_add}/api/{project}/testcase_result/%s/' % case_result_obj['id']).format(server_add=SERVER, project='Media')
    # writer 'result', 'bug', 'log' information for testcase
    case_result_obj['result'] = 'pass'
    case_result_obj['bug'] = '1.5.1 bug'
    case_result_obj['log'] = '1.5.1 log'
    case_result_obj['comments'] = '1.5.1 test'

    r = requests.put(url, case_result_obj, auth=HTTPBasicAuth(username, password))
    print r.status_code
    print r.text


def run_testplan(plan_id, name, os, platform, runner, project, performance, app):
    exe_id = create_execution(plan_id=plan_id, name=name, os=os, platform=platform,
                              runner=runner, project=project, performance=performance, app=app)
    if exe_id:
        suite_result_list = get_suite_result(execution_id=exe_id)
        for suite_result_obj in suite_result_list:
            case_result_list = get_case_result(suite_result_obj['id'])
            for case_result_obj in case_result_list:
                save_case_result(case_result_obj=case_result_obj)
    else:
        print 'create execution fail.'


def get_req_type():
    url = '{server_add}/api/{project}/requirement_type/'.format(server_add=SERVER, project='DPDK')
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    print r.status_code
    print r.json()


def get_perf_suite_result(exe_id):
    url = ('{server_add}/api/{project}/testexecution_perf_suite_result/%s/' % exe_id).format(server_add=SERVER, project='Media')
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    print '===================='
    print r
    print '===================='
    print r.json()
    return r.json()


def get_appattr(app_id):
    url = '{server_add}/api/{project}/app_attr/'.format(server_add=SERVER, project='Media')
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    print '===================='
    print r
    print '===================='
    print r.json()
    attr_list = []
    for item in r.json():
        if item['app'] == int(app_id):
            attr_list.append((item['id']))
    return attr_list


def get_perf_case_detail_list(case_result_obj):
    url = ('{server_add}/api/{project}/perf_caseresult_detailresult/%s/' % case_result_obj['id']).format(server_add=SERVER, project='Media')
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    print '===================='
    print r
    print '===================='
    print r.json()
    return r.json()


def run_perf_testcase(case_result_obj):
    # writer 'bug', 'log', 'comments' information for testcase
    url = ('{server_add}/api/{project}/perf_testcase_result/%s/' % case_result_obj['id']).format(server_add=SERVER, project='Media')
    case_result_obj['bug'] = '1.5.1 perf bug'
    case_result_obj['log'] = '1.5.1 perf log'
    case_result_obj['comments'] = '1.5.1 perf comments'

    r = requests.put(url, case_result_obj, auth=HTTPBasicAuth(username, password))
    print '===================='
    print r
    print '===================='
    print r.json()

    detail_obj_list = get_perf_case_detail_list(case_result_obj)
    for detail_obj in detail_obj_list:
        save_perf_case_attr_result(detail_obj)


def save_perf_case_attr_result(detail_obj):
    url = ('{server_add}/api/{project}/perf_testcase_result_detail/%s/' % detail_obj['id']).format(server_add=SERVER, project='Media')
    # writer attr_value
    detail_obj['value'] = '80.00'

    r = requests.put(url, detail_obj, auth=HTTPBasicAuth(username, password))
    print '===================='
    print r
    print '===================='
    print r.json()


def run_perf_testplan(plan_id, name, os, platform, runner, project, performance, app):
    exe_id = create_execution(plan_id=plan_id, name=name, os=os, platform=platform, runner=runner, project=project,
                              performance=performance, app=app)
    if exe_id:
        suite_result_list = get_perf_suite_result(exe_id)
        for suite_result_obj in suite_result_list:
            case_result_list = get_perf_case_result(suite_result_obj['id'])
            for case_result_obj in case_result_list:
                run_perf_testcase(case_result_obj)
    else:
        print "create execution fail"


def main():
    #run_perf_testplan(plan_id=150, name='exe_plan_150', os=3, platform=3, runner='zwang18x', project=1, performance=True, app=2)
    #run_testplan(plan_id=135, name='function_plan_135', os=3, platform=3, runner='zwang18x', project=1, performance=False, app=None)
    get_project_list()
    get_testplan_list()
    #get_suite_result(1)
    #run_testplan(plan_id=3, name='dpdk_testplan', os=1, platform=1,runner='wuwenzhong', project=1, performance=True, app=None)
    #get_req_type()
    #new_dpdk_testplan()
    #new_dpdk_testplan(4,"test_api",1,True,1,'admin',"2016-10-28T15:48:027","2016-10-28T15:48:027","2016-10-28T15:48:027","null")
#def create_execution(plan_id, name, os, platform, runner, project, performance, app):
    #create_execution(1,"dpdk4",1,1,"admin",1,True,1)
    new_dpdk_testresult()
    #get_project_list()
    #get_perf_suite_result(1)
    #new_dpdk_testresult(2,1,1,6,21,1,1,27,"2016-10-28T15:48:027")
if '__main__' == __name__:
    main()
