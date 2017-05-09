import requests
import json


def process_worker_detail(context, worker_info):
    worker_list = worker_info['worker_list']
    worker_detail = []
    for worker in worker_list:
        os_str = nic_str = kernel_str = target_str = gcc_str = driver_str = platform_str = ""
        detail = worker_info[worker]
        for os in detail['os']:
            os_str += "; " + os
        for nic in detail['nic']:
            nic_str += "; " + nic
        for kernel in detail['kernel']:
            kernel_str += "; " + kernel
        for target in detail['target']:
            target_str += "; " + target
        for gcc in detail['gcc']:
            gcc_str += "; " + gcc
        for driver in detail['driver']:
            driver_str += "; " + driver
        for platform in detail['platform']:
            platform_str += "; " + platform
        worker_detail.append({
            'name': worker,
            'os': os_str.lstrip("; "),
            'nic': nic_str.lstrip("; "),
            'kernel': kernel_str.lstrip("; "),
            'target': target_str.lstrip("; "),
            'gcc': gcc_str.lstrip("; "),
            'driver': driver_str.lstrip("; "),
            'platform': platform_str.lstrip("; "),
        })
    context['worker_detail'] = worker_detail
    return context


def process_data(context, worker_info, worker):
    worker_list = worker_info['worker_list']
    os_list, nic_list, kernel_list, test_type_list = [], [], [], []
    target_list, gcc_list, driver_list, platform_list, gitrepo_list = [], [], [], [], []

    if worker and worker in worker_list:
        # have worker
        detail = worker_info[worker]
        os_list = detail['os']
        nic_list = detail['nic']
        kernel_list = detail['kernel']
        test_type_list = detail['test_type']
        target_list = detail['target']
        gcc_list = detail['gcc']
        driver_list = detail['driver']
        platform_list = detail['platform']
        gitrepo_list = detail.get('gitrepo', None)
    else:
        # no worker or worker not exist, return all worker info
        # get config lists and remove the dup items
        for worker in worker_list:
            info = worker_info[worker]
            for os in info['os']:
                if os not in os_list:
                    os_list.append(os)
            for nic in info['nic']:
                if nic not in nic_list:
                    nic_list.append(nic)
            for kernel in info['kernel']:
                if kernel not in kernel_list:
                    kernel_list.append(kernel)
            for type in info['test_type']:
                if type not in test_type_list:
                    test_type_list.append(type)
            for target in info['target']:
                if target not in target_list:
                    target_list.append(target)
            for gcc in info['gcc']:
                if gcc not in gcc_list:
                    gcc_list.append(gcc)
            for driver in info['driver']:
                if driver not in driver_list:
                    driver_list.append(driver)
            for platform in info['platform']:
                if platform not in platform_list:
                    platform_list.append(platform)
            for gitrepo in info.get('gitrepo', None):
                if gitrepo not in gitrepo_list:
                    gitrepo_list.append(gitrepo)

    context['worker_info'] = json.dumps(worker_info)
    context['worker_list'] = worker_list
    context['os_list'] = os_list
    context['nic_list'] = nic_list
    context['kernel_list'] = kernel_list
    context['test_type_list'] = test_type_list
    context['target_list'] = target_list
    context['gcc_list'] = gcc_list
    context['driver_list'] = driver_list
    context['platform_list'] = platform_list
    context['gitrepo_list'] = gitrepo_list

    return context


def get_itec_info(ip):
    url = 'http://127.0.0.1:8080/itec/' + ip
    r = requests.get(url)
    print r.url
    print r.status_code
    print r.text
    return r.text


def post_env_setting(para):
    url = 'http://127.0.0.1:8080/itms_setting'
    r = requests.post(url, para)
    print r.url
    print r.status_code
    print r.text
