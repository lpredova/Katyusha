from pysimplesoap.client import SoapClient
from payloadreader import PayloadReader
from fuzzer import Fuzzer
from helpers import Helper

import time

__author__ = "Milan"

class SoapFuzzer(Fuzzer):

    _wsdl = ""
    _ops_and_args = {}
    _ops_to_fuzz = {}

    def __init__(self):
        Fuzzer.__init__(self)
        self.method = "POST" # SOAP uses POST

    def get_ops_and_args(self):
        for service in self._soap_client.services.values():
            for port in service['ports'].values():
                for op in port['operations'].values():
                    op_name = op['name']
                    op_args = []
                    for input_msg in op['input']:
                        for arg in op['input'][input_msg]:
                            op_args.append(arg)
                    self._ops_and_args[op_name] = op_args

    def get_operations_to_fuzz(self):
        for operation in self._ops_and_args.keys():
            prompt = "Do you want to fuzz operation {} ? (y/n) ".format(operation)
            fuzz_operation = raw_input(prompt).capitalize()
            fuzz_any_op_arg = 0
            args_to_fuzz = {}
            if fuzz_operation == 'Y':
                for arg in self._ops_and_args[operation]:
                    prompt = "Fuzz argument {} ? (y/n) ".format(arg)
                    fuzz_arg = raw_input(prompt).capitalize()
                    if fuzz_arg == 'Y':
                        fuzz_any_op_arg = 1
                    if fuzz_arg != 'Y' and fuzz_arg != 'N':
                        fuzz_arg = 'N'
                    args_to_fuzz[arg] = fuzz_arg
                if fuzz_any_op_arg == 1:
                    self._ops_to_fuzz[operation] = args_to_fuzz
            print
        #print(self._ops_to_fuzz)

    def get_fuzz_vectors(self):
        reader = PayloadReader()
        #vectors = ["'", "or 1=1", "1'or'1'='1", "admin", "1' and 1=(select count(*) from tablenames); --"] #TODO hardcoded, fix this !!
        vectors = reader.get_fuzz_strings()
        return vectors

    def send_requests(self):
        result = []
        errors = 0
        fuzz_vectors = self.get_fuzz_vector()
        for operation in self._ops_to_fuzz:
            print("Fuzzing operation {}...".format(operation)) # remove ?
            soap_operation = getattr(self._soap_client, str(operation))
            for vector in fuzz_vectors:
                try:
                    kwargs = {}
                    args = self._ops_to_fuzz[operation]
                    for arg_name in args.keys():
                        if args[arg_name] == 'Y':
                            kwargs[arg_name] = str(vector)
                        elif args[arg_name] == 'N' and vector == "'": # TODO dirty fix for "'" parsing; remove in future
                            kwargs[arg_name] = str(vector)

                    print kwargs # TODO remove
                    start_time = time.time()
                    response = soap_operation(**kwargs)
                    end_time = time.time()
                    response_time = format(end_time - start_time, '.4f')

                    result.append({
                        'request': self._soap_client.xml_request,
                        'status': False, # TODO what does it mean ?
                        'method': self.method,
                        'id': self.request_id,
                        'time': response_time,
                        'code': self._soap_client.response['status'],
                        'response': response,
                        'headers': {
                            'x-powered-by': self._soap_client.response['x-powered-by'],
                            'set-cookie': self._soap_client.response['set-cookie'],
                            'connection': '(unknown)', # isn't available in response
                            'host (server)': self._soap_client.response['server'], # host = server ?
                            'x-soap-server': self._soap_client.response['x-soap-server'], # added for soap
                            'cache-control': self._soap_client.response['cache-control'],
                            'date': self._soap_client.response['date'],
                            'content-type': self._soap_client.response['content-type']
                        },
                        'length (xml response)': self._soap_client.response['content-length']
                    })

                    self.request_id += 1

                #print(response)
                #print(self._soap_client.xml_response)
                #print(response_time)
                #print(self._soap_client.xml_request)
                #print(self._soap_client.response)
                #print

                except:
                    errors += 1
                    print("Error occured for fuzz vector: " + vector)
                    result.append({
                            'request': self._soap_client.xml_request,
                            'status': False, # TODO what does it mean ?
                            'method': self.method,
                            'id': self.request_id,
                            'time': 'error',
                            'code': self._soap_client.response['status'],
                            'response': 'error',
                            'headers': {
                                'x-powered-by': 'error',
                                'set-cookie': 'error',
                                'connection': 'error',
                                'host (server)': 'error',
                                'x-soap-server': 'error',
                                'cache-control': 'error',
                                'date': 'error',
                                'content-type': 'error'
                            },
                            'length (xml response)': 0
                        })
                    self.request_id += 1
        print(result) # TODO remove
        print "\nFuzzing done. Errors: %d" % errors
        return result

    def start_fuzzing(self):

        Helper.delimiter_line()
        print "SOAP FUZZER"
        Helper.delimiter_line()

        self._wsdl = raw_input("WSDL URL: ")
        print("Please wait...")
        self._soap_client = SoapClient(wsdl = self._wsdl)

        self.get_ops_and_args()
        self.get_operations_to_fuzz()
        results = self.send_requests()

        self.save_data(results, "soap")
        self.present_results()



# just for testing, will be removed in final version
#sf = SoapFuzzer()
#sf.start_fuzzing()

