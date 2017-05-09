import web
import json
import logging
import os


def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.")


def internalerror():
    return web.internalerror("Bad, bad server. No donut for you.")


def iteclog(data):
    if os.path.exists('itec.log'):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='itec.log',
                            filemode='a')
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='itec.log',
                            filemode='w')
    logging.info(data)


urls = (
    '/(.*)/', 'redirect',
    '/itec/(.+)', 'Worker',                 # eg. /itec/10.239.119.216
    '/worker_detail/ip=(.*)&worker=(.*)', 'WorkerDetail',  # eg. /worker_detail/ip=10.239.119.219&worker=name
    '/itms_setting', 'Environment'
)

app = web.application(urls, globals())
app.notfound = notfound
app.internalerror = internalerror


class redirect:
    def GET(self, path):
        web.seeother('/' + path)


class Worker:
    def GET(self, ip):
        payload = {
            'worker_list': ['worker1', 'worker2'],
            'worker1': {
                'os': ['UB1510'],
                'kernel': ['4.2.0-16-generic'],
                'gcc': ['5.2.1'],
                'target': ['x86_64-native-linuxapp(bsdapp)-gcc'],
                'nic': ['Niantic'],
                'test_type': ['Smoke'],
                'driver': ['1.2.1'],
                'platform': ['Haswell'],
                'gitrepo': ['0.1']
            },
            'worker2': {
                'os': ['SuSe12', 'FreeBSD10'],
                'kernel': ['3.12.28-4-default', '10.2-RELEASE'],
                'gcc': ['4.8.3', '4.8.5'],
                'target': ['x86_64-native-linuxapp(bsdapp)-gcc', 'x86_64-native-linuxapp-icc'],
                'nic': ['Niantic', 'Borb'],
                'test_type': ['Smoke', 'Functional'],
                'driver': ['1.2.1', '1.0'],
                'platform': ['IvyBridge', 'Broadwell'],
                'gitrepo': ['0.1', '0.2']
            }
        }
        return json.dumps(payload)

    def POST(self):
        data = web.data()
        print data
        return data


class WorkerDetail:
    def GET(self, ip, worker):
        payload = {
            'os': ['UB1510'],
            'kernel': ['4.2.0-16-generic '],
            'gcc': ['5.2.1'],
            'target': ['x86_64-native-linuxapp(bsdapp)-gcc'],
            'nic': ['Niantic'],
            'test_type': ['Smoke'],
            'driver': ['1.2.1'],
            'platform': ['Haswell'],
            'gitrepo': ['0.1']
        }
        return json.dumps(payload)

    def POST(self):
        data = web.data()
        print data
        return data


class Environment:
    def POST(self):
        data = web.input()
        iteclog(data)
        print data
        return data

if __name__ == '__main__':
    app.run()




