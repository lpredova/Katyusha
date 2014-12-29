__author__ = 'lovro'

from validator import Validator
from helpers import Helper
from fuzzer import Fuzzer


class RestFuzzer(Fuzzer):
    api_url = ""

    def __init__(self):
        Fuzzer.__init__(self)

    def get_url(self):

        while 1:
            url = raw_input("Please insert URL to API :")
            validator = Validator()
            if validator.validate_url(url):
                self.api_url = url
                return 0

    def get_method(self):
        while 1:
            method = Helper.create_prompt('Method', 'GET', 'POST', 'Quit')
            if method == '1':
                self.method = 'GET'
                return 0
            elif method == '2':
                self.method = 'POST'
                return 0
            elif method == '3':
                Helper.confirm_quit()

    def insert_params(self):
        more = True
        while more:

            Helper.delimiter_line()
            key = raw_input('Name of the parametar you want to fuzz :')
            fuzz = raw_input('Fuzz this parameter (Y/N):')
            if fuzz == 'Y' or fuzz == 'y' or fuzz == 'yes':
                self.request_params[key] = 'fuzz'
            else:
                self.request_params[key] = ''

            m = raw_input('Add more parameters (Y/N) ? ')
            if m == 'Y' or m == 'y' or m == 'yes' or m == '1':
                more = True
            else:
                more = False
        return 0

    # MAIN
    def start_fuzzing(self):

        Helper.delimiter_line()
        print "REST FUZZER"
        Helper.delimiter_line()

        self.get_url()
        self.get_method()
        self.insert_params()

        results = self.send_requests()
        self.save_data(results, "rest")
        if not self.present_results():
            return 0




