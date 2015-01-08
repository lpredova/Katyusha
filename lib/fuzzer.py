import urllib

__author__ = 'lovro'

from abc import ABCMeta
from helpers import Helper
from localserver import Server
from payloadreader import PayloadReader

import requests
import webbrowser
import threading
import json
import datetime
import time
import os


class Fuzzer():
    __metaclass__ = ABCMeta

    api_url = ""
    method = ""

    request_params = {}
    modified_request = []

    _result_file = ""
    request_id = 1

    def __init__(self):
        pass

    def send_requests(self):

        response_time = ""
        result = []
        print "Fuzzing started..."

        fuzz_vector = self.get_fuzz_vector()
        for vector in fuzz_vector:
            fuzz_request = self.switch_param(vector)
            #print fuzz_request

            try:
                if self.method == 'GET':
                    start_request = time.time()
                    r = requests.get(self.api_url, data=json.dumps(fuzz_request))
                    end_request = time.time()
                    response_time = format(end_request - start_request, '.4f')

                elif self.method == 'POST':
                    start_request = time.time()
                    r = requests.post(self.api_url, data=json.dumps(fuzz_request))
                    end_request = time.time()
                    response_time = format(end_request - start_request, '.4f')

                result.append({'request': fuzz_request,
                               'status': False,
                               'method': self.method,
                               'id': self.request_id,
                               'time': response_time,
                               'code': r.status_code,
                               'response': r.text,
                               'headers': {
                                   'x-powered-by': r.headers['x-powered-by'],
                                   'set-cookie': r.headers['set-cookie'],
                                   'connection': r.headers['connection'],
                                   'host': r.headers['host'],
                                   'cache-control': r.headers['cache-control'],
                                   'date': r.headers['date'],
                                   'content-type': r.headers['content-type']
                               },
                               'length': len(r.text)})

            except:
                result.append({'request': fuzz_request,
                               'status': False,
                               'method': self.method,
                               'id': self.request_id,
                               'time': response_time,
                               'code': r.status_code,
                               'response': r.text,
                               'headers': {
                                   'x-powered-by': r.headers['x-powered-by'],
                                   'set-cookie': r.headers['set-cookie'],
                                   'connection': r.headers['connection'],
                                   'host': "error",
                                   'cache-control': r.headers['cache-control'],
                                   'date': r.headers['date'],
                                   'content-type': r.headers['content-type']
                               },
                               'length': len(r.text)})
            self.request_id += 1
            time.sleep(0.01)

        # ##Printig params
        print "Fuzzing done..."
        return result

    def switch_param(self, vector):
        items = {}
        for key, value in self.request_params.items():
            if key == "":
                continue
            if value == 'fuzz':
                items[key] = vector
            else:
                items[key] = ''
        return items

    def get_fuzz_vector(self):
        reader = PayloadReader()
        strings = reader.get_fuzz_strings()
        return strings

    def save_data(self, result, service_type):
        ts = time.time()

        try:
            current_time = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
            self._result_file = service_type + '_result_' + current_time + '.json'

            with open('results/' + self._result_file, 'w') as outfile:
                json.dump(result, outfile)

            print "Results saved at: 'results/'" + self._result_file
        except Exception:
            print "Ooops ! There was a problem with saving results."

    def present_results(self):
        while 1:
            method = Helper.create_prompt('View results', 'YES', 'NO','Quit')
            if method == '1':
                self.open_results()
            elif method == '2':
                return 0
            elif method == '3':
                Helper.confirm_quit()

    def open_results(self):

        print 'Find results at:\n' + 'http://localhost:8088/#/' + self._result_file

        server = Server()
        threading.Thread(target=server.serve()).start()

        try:
            webbrowser.open('http://localhost:8088/#/' + self._result_file, 2)
        except:
            print 'Find results at:\n http://localhost:8088/#/' + self._result_file
            return 0