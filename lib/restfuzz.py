__author__ = 'lovro'

from pywebfuzz import utils

class RestFuzzer:
    def __init__(self):
        pass

    def start_fuzzing(self):
        print "fuzzing rest"


        #https://code.google.com/p/pywebfuzz/wiki/UsageExamples
        result = utils.make_request('http://localhost:8000/api/v1/locations')

        #print( headers)
        print result
