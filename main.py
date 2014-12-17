__author__ = 'lovro'
# Naming convention https://www.python.org/dev/peps/pep-0008/
from lib.validator import Validator
from lib.soapfuzz import SoapFuzzer
from lib.restfuzz import RestFuzzer
from lib.helpers import Helper


class MainMenu:
    api_url = ""

    def __init__(self):
        pass

    def get_url(self):

        while 1:
            self.api_url = raw_input("Please insert URL to API :")

            validator = Validator()
            if validator.validate_url(self.api_url):
                protocole = Helper.create_prompt(
                    "Please choose your protocole",
                    "REST", "SOAP"
                )

                if protocole == '1':
                    rest = RestFuzzer(self.api_url)
                    rest.start_fuzzing()

                elif protocole == '2':
                    soap = SoapFuzzer()
                    soap.start_fuzzing()
                else:
                    print "Nice try..."
                    Helper.delimiter_line()
            else:
                Helper.error_message("Invalid URL !")



if __name__ == '__main__':
    menu = MainMenu()

    Helper.welcome_message()
    Helper.delimiter_line()

    while 1:
        mode = Helper.create_prompt(
            "Please choose your action",
            "Fuzz API service", "Quit")

        if mode == '1':
            menu.get_url()

        elif mode == '2':
            Helper.confirm_quit()

        elif mode == 'sssr':
            Helper.play_me_something()

        else:
            print "Hey hey, let's focus here,shall we?"
            Helper.delimiter_line()