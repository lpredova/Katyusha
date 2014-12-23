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
    params = []
    _result_file = ""

    def __init__(self):
        pass

    def send_requests(self):
        result = []

        print "Fuzzing started...Please wait..."

        fuzz_vector = self.get_fuzz_vector()
        print fuzz_vector

        # TODO this loop should go through entire results list and query for each param 0-5 is just for testing
        for x in range(0, 5):
            try:

                if self.method == 'GET':
                    r = requests.get(self.api_url, data=json.dumps(self.params))
                    #print r.headers
                    #print r.cookies

                elif self.method == 'POST':
                    r = requests.post(self.api_url, data=json.dumps(self.params))

                # TODO ovdje u request ide array onoga sto smo pitali server
                result.append({'request': 'array(nesto)',
                               'status': False,
                               'id': x,
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
                result.append({'request': 'rekvest',
                               'status': 'error',
                               'id': 'error',
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
        ###Printig params
        print self.params


        print "Fuzzing done..."
        return result

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