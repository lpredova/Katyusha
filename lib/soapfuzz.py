from pysimplesoap.client import SoapClient
from payloadreader import PayloadReader

__author__ = "Milan"

class SoapFuzzer:

    _wsdl = ""
    _ops_and_args = {}
    _ops_to_fuzz = {}

    def __init__(self):
        pass

    def get_wsdl(self):
        return self._wsdl

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
        print(self._ops_to_fuzz)

    def get_fuzz_vectors(self):
        reader = PayloadReader()
        vectors = ["'", "or 1=1", "1'or'1'='1", " a "] #TODO hardcoded, fix this !!
        return vectors

    def fuzz_operations(self):
        fuzz_vectors = self.get_fuzz_vectors()
        for operation in self._ops_to_fuzz:
            print("Fuzzing operation {}...".format(operation)) # remove ?
            soap_operation = getattr(self._soap_client, str(operation))
            for vector in fuzz_vectors:
                kwargs = {}
                args = self._ops_to_fuzz[operation]
                for arg_name in args.keys():
                    if(args[arg_name] == 'Y'):
                        kwargs[arg_name] = vector
                    #else:
                    #    kwargs[arg_name] = vector # error is thrown for ' ?
                print kwargs # TODO remove
                response = soap_operation(**kwargs)
                print(response) # for item in response print item and response[item] ?


    def start_fuzzing(self):
        self._wsdl = raw_input("WSDL URL: ")
        print("Please wait...")
        self._soap_client = SoapClient(wsdl = self._wsdl)
        self.get_ops_and_args()
        self.get_operations_to_fuzz()
        self.fuzz_operations()



# just for testing, will be removed in final version
sf = SoapFuzzer()
sf.start_fuzzing()

