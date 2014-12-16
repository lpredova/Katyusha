__author__ = 'lovro'

from localserver import Server
from helpers import Helper
import httplib2
import urllib
import json
import datetime
import time
import webbrowser
import threading


class RestFuzzer():
    method = ""
    result_file = ""

    def __init__(self):
        pass

    def get_method(self):
        while 1:
            method = Helper.create_prompt('Method', 'GET', 'POST')
            if method == '1':
                return 'GET'
            elif method == '2':
                return 'POST'

    def open_results(self):

        print 'Find results at:\n' + 'http://localhost:8080/#/' + self.result_file

        server = Server()
        threading.Thread(target=server.serve()).start()

        try:
            urllib.quote_plus('$#@=?%^Q^$')

            webbrowser.open('http://localhost:8080/#/' + self.result_file, 2)
        except:
            print 'Find results at:\n http://localhost:8080/#/' + self.result_file

    def save_data(self, result):
        ts = time.time()
        current_time = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
        self.result_file = 'rest_fuzz_result_' + current_time + '.json'

        with open('results/' + self.result_file, 'w') as outfile:
            json.dump(result, outfile)

    def present_results(self):
        while 1:
            method = Helper.create_prompt('Do you want to view results', 'YES', 'NO')
            if method == '1':
                self.open_results()
            elif method == '2':
                return 0

    def send_requests(self):

        result = []
        for x in range(0, 5):
            try:
                h = httplib2.Http(".cache")
                resp, content = h.request('http://localhost:8000/api/v1/locations', "GET")

                item = {'id': x, 'response': resp, 'content': content, 'length': len(content)}
                result.append(item)

            except:
                result.append("error")

        return result


    # Main method in rest fuzzer class
    def start_fuzzing(self):

        Helper.delimiter_line()
        print "REST FUZZER"
        Helper.delimiter_line()

        self.method = self.get_method()
        results = self.send_requests()
        print results

        self.save_data(results)
        self.present_results()



