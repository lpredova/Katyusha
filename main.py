__author__ = 'lovro'
# Naming convention https://www.python.org/dev/peps/pep-0008/
from lib.soapfuzz import SoapFuzzer
from lib.restfuzz import RestFuzzer
from lib.helpers import Helper
from lib.proxy import ProxyListener


class MainMenu:
    def __init__(self):
        pass

    def get_url(self):

        while 1:
            protocole = Helper.create_prompt(
                "Please choose your protocole",
                "REST", "SOAP", "Quit"
            )

            if protocole == '1':
                rest = RestFuzzer()
                rest.start_fuzzing()

            elif protocole == '2':
                soap = SoapFuzzer()
                soap.start_fuzzing()

            elif protocole == '3':
                Helper.confirm_quit()

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
            "Fuzz API service",
            "Listen as Proxy",
            "Quit")

        if mode == '1':
            menu.get_url()

        elif mode == '2':
            ProxyListener.listen_communication()

        elif mode == '3':
            Helper.confirm_quit()

        elif mode == 'sssr':
            Helper.play_me_something()

        else:
            print "Hey hey, let's focus here,shall we?"
            Helper.delimiter_line()