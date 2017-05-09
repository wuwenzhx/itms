
Quick Start
===============

With REST api, we can edit test data automatically. Here are two demos for normal perf test case and DPDK perf test
case for your reference.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Normal Perf demo
~~~~~~~~~~~~~~~~~~

This automation script it used to create perf test result for normal perf test case.

.. code-block:: python
    :linenos:

    import requests
    import json
    from requests.auth import HTTPBasicAuth

    SERVER = 'http://127.0.0.1:8000'
    username = 'xxxxxxxx'
    password = 'xxxxxxxx'

    def create_execution(plan_id, name, os, platform, runner, project, performance, app):
        url = '{server_add}/api/{project}/testexecution/'.format(server_add=SERVER, project='Media')
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


    def get_perf_suite_result(exe_id):
        url = ('{server_add}/api/{project}/testexecution_perf_suite_result/%s/' % exe_id).
                format(server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth(username, password))
        print '===================='
        print r
        print '===================='
        print r.json()
        return r.json()


    def get_perf_case_result(suite_reuslt_id):
        url = ('{server_add}/api/{project}/perf_suiteresult_caseresult/%s/' % suite_reuslt_id).format(
                server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth(username, password))
        print r.json()
        return r.json()


    def run_perf_testcase(case_result_obj):
        # writer 'bug', 'log', 'comments' information for testcase
        url = ('{server_add}/api/{project}/perf_testcase_result/%s/' % case_result_obj['id']).format(
                server_add=SERVER, project='Media')
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


    def get_perf_case_detail_list(case_result_obj):
        url = ('{server_add}/api/{project}/perf_caseresult_detailresult/%s/' % case_result_obj['id']).format(
                server_add=SERVER, project='Media')
        r = requests.get(url, auth=HTTPBasicAuth(username, password))
        print '===================='
        print r
        print '===================='
        print r.json()
        return r.json()


    def save_perf_case_attr_result(detail_obj):
        url = ('{server_add}/api/{project}/perf_testcase_result_detail/%s/' % detail_obj['id']).format(
                server_add=SERVER, project='Media')
        # writer attr_value
        detail_obj['value'] = '80.00'

        r = requests.put(url, detail_obj, auth=HTTPBasicAuth(username, password))
        print '===================='
        print r
        print '===================='
        print r.json()


    def run_perf_testplan(plan_id, name, os, platform, runner, project, performance, app):
        exe_id = create_execution(plan_id=plan_id, name=name, os=os, platform=platform, runner=runner,
                                  project=project, performance=performance, app=app)
        if exe_id:
            suite_result_list = get_perf_suite_result(exe_id)
            for suite_result_obj in suite_result_list:
                case_result_list = get_perf_case_result(suite_result_obj['id'])
                for case_result_obj in case_result_list:
                    run_perf_testcase(case_result_obj)
        else:
            print "create execution fail"


    def main():
        run_perf_testplan(plan_id=83, name='exe_1.5.1_10', os=3, platform=3, runner='api',
                          project=1, performance=True, app=1)

    if '__main__' == __name__:
        main()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DPDK Perf demo
~~~~~~~~~~~~~~~

For DPDK perf test case result, there is a little difference in result detail structure, this automation script is
only for DPDK.

.. code-block:: python
    :linenos:

    import requests
    import json
    from requests.auth import HTTPBasicAuth

    SERVER = 'http://127.0.0.1:8000'
    username = 'xxxxxxxx'
    password = 'xxxxxxxx'
    packset_size_list = [64, 128, 256, 512, 1024, 1280, 1518]


    def get_appattr(app_id):
        url = '{server_add}/api/{project}/app_attr/'.format(server_add=SERVER, project='DPDK')
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

    def save_perf_dpdk_case_attr_result(case_result_id, app, packset_size_id):

        group_id = None
        key_id = None
        value = None
        #get app
        attr_list = get_appattr(app)

        group_id = 1
        for packset_size in packset_size_list:
            for attr in attr_list:
                key_id = attr
                if attr == packset_size_id:
                    value = packset_size
                else:
                    value = '46.23'
                save_perf_dpdk_detail_result(case_result_id, key_id, value, group_id, app)
            group_id += 1


    def save_perf_dpdk_detail_result(case_result_id, key_id, value, group_id, app):
        url = '{server_add}/api/{project}/perf_dpdk_testcase_result_detail/'.format(
                server_add=SERVER, project='DPDK')
        payload = {'perf_dpdk_testcase_result': case_result_id, 'key': key_id, 'value': value,
                   'app': app, 'group': group_id}
        r = requests.post(url, payload, auth=HTTPBasicAuth(username, password))
        print r.url
        print r.json()


    def get_perf_dpdk_case_result(suite_reuslt_id):
        url = ('{server_add}/api/{project}/perf_dpdk_suiteresult_caseresult/%s/' % suite_reuslt_id).format(
                 server_add=SERVER, project='DPDK')
        r = requests.get(url, auth=HTTPBasicAuth(username, password))
        print r.json()
        case_result_list = []
        for item in r.json():
            case_result_list.append((item['id']))
        return case_result_list

    def run_perf_dpdk_testplan(plan_id, name, os, platform, runner, project, performance, app, packset_size_id):
        exe_id = create_execution(plan_id=plan_id, name=name, os=os, platform=platform, runner=runner,
                                  project=project, performance=performance, app=app)
        if exe_id:
            suite_result_list = get_perf_suite_result(exe_id)
            for suite_result_id in suite_result_list:
                print suite_result_id
                case_result_list = get_perf_dpdk_case_result(suite_result_id)
                for case_result_id in case_result_list:
                    save_perf_dpdk_case_attr_result(case_result_id, app, packset_size_id)
        else:
            print "create execution fail"


    def main():
        run_perf_dpdk_testplan(plan_id=103, name='perf_dpdk_exe_1.14', os=9, platform=5, runner='api',
                               project=2, performance=True, app=5, packset_size_id=12)

        if '__main__' == __name__:
            main()