__author__ = 'lovro'

import httplib2
import json
import datetime
import time

from pywebfuzz import utils


class RestFuzzer:
    def __init__(self):
        pass

    def start_fuzzing(self):
        print "fuzzing rest"


        # https://code.google.com/p/pywebfuzz/wiki/UsageExamples
        # result = utils.make_request('http://localhost:8000/api/v1/locations')

        result = []

        for x in range(0, 5):
            h = httplib2.Http(".cache")
            resp, content = h.request('http://localhost:8000/api/v1/locations', "GET")

            item = {'id': x, 'response': resp, 'content': content, 'length': len(content)}
            result.append(item)

        #resopnse
        #print resp

        #response content
        print result

        ts = time.time()
        current_time = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
        with open('results/rest_fuzz_result_'+current_time+'.json', 'w') as outfile: json.dump(result, outfile)
