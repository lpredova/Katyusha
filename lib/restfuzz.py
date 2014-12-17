__author__ = 'lovro'

from helpers import Helper
from fuzzer import Fuzzer


class RestFuzzer(Fuzzer):

    def __init__(self, url):
        self.api_url = url
        Fuzzer.__init__(self)

    def get_method(self):
        while 1:
            method = Helper.create_prompt('Method', 'GET', 'POST')
            if method == '1':
                self.method = 'GET'
                return 0
            elif method == '2':
                self.method = 'POST'
                return 0

    # TODO - adding multiple params and marking which params we want to attack
    def insert_params(self):
        print "inserting params"
        self.params = {'user': 'admin', 'password': 'admin'}

        return 0

    # Main method in rest fuzzer class
    def start_fuzzing(self):

        Helper.delimiter_line()
        print "REST FUZZER"
        Helper.delimiter_line()

        self.get_method()
        self.insert_params()

        results = self.send_requests()
        self.save_data(results)
        self.present_results()



