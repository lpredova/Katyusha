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
        result = []
        print "Fuzzing started..."

        fuzz_vector = self.get_fuzz_vector()
        for vector in fuzz_vector:
            fuzz_request = self.switch_param(vector)
            print fuzz_request

            try:
                if self.method == 'GET':
                    r = requests.get(self.api_url, data=json.dumps(fuzz_request))

                elif self.method == 'POST':
                    r = requests.post(self.api_url, data=json.dumps(fuzz_request))

                result.append({'request': fuzz_request,
                               'status': False,
                               'id': self.request_id,
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
                self.request_id += 1

            except:
                result.append({'request': fuzz_request,
                               'status': 'error',
                               'id': self.request_id,
                               'code': r.status_code,
                               'response': 'error',
                               'headers': {
                                   'x-powered-by': 'error',
                                   'set-cookie': 'error',
                                   'connection': 'error',
                                   'host': 'error',
                                   'cache-control': 'error',
                                   'date': 'error',
                                   'content-type': 'error'
                               },
                               'length': 0})
                self.request_id += 1

        # ##Printig params
        print self.request_params

        print "Fuzzing done..."
        return result

    def switch_param(self, vector):
        items = {}
        print "rekvest params original :"
        print self.request_params
        print "\n"

        for key, value in self.request_params.items():
            print "key: "+ key + " value :" + value

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

    def save_data(self, result):
        ts = time.time()

        current_time = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
        self._result_file = 'rest_result_' + current_time + '.json'

        with open('results/' + self._result_file, 'w') as outfile:
            json.dump(result, outfile)

    def present_results(self):
        while 1:
            method = Helper.create_prompt('Do you want to view results', 'YES', 'NO')
            if method == '1':
                self.open_results()
            elif method == '2':
                return 0

    def open_results(self):

        print 'Find results at:\n' + 'http://localhost:8080/#/' + self._result_file

        server = Server()
        threading.Thread(target=server.serve()).start()

        try:
            webbrowser.open('http://localhost:8080/#/' + self._result_file, 2)
        except:
            print 'Find results at:\n http://localhost:8080/#/' + self._result_file
            return 0