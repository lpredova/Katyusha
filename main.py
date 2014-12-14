__author__ = 'lovro'
# Naming convention https://www.python.org/dev/peps/pep-0008/
import sys

from validator import Validator
from soapfuzz import SoapFuzzer
from restfuzz import RestFuzzer
import webbrowser


class MainMenu:
    api_url = ""

    @property
    def welcome_message(self):
        logo = "  _   __      _                   _           \n" \
               " | | / /     | |                 | |          \n" \
               " | |/ /  __ _| |_ _   _ _   _ ___| |__   __ _ \n" \
               " |    \ / _` | __| | | | | | / __|  _ \ / _` |\n" \
               " | |\  \ (_| | |_| |_| | |_| \__ \ | | | (_| |\n" \
               " \_| \_/\__,_|\__|\__, |\__,_|___/_| |_|\__,_|\n" \
               "                   __/ |                      \n" \
               "                  |___/                       \n" \
               "REST and SOAP fuzzer                          \n"
        return logo

    @property
    def delimiter_line(self):
        return "################################################"


    @staticmethod
    def create_prompt(message, option1, option2):
        options = "\n" + message + ":\n" \
                                   "1) " + option1 + "\n" \
                                                     "2) " + option2 + "\n" \
                                                                       "Select:"
        return raw_input(options)


    @staticmethod
    def error_message(error):
        print "Sorry there has been an error : " + error + "\n"
        print menu.delimiter_line

    @staticmethod
    def play_me_something():
        webbrowser.open("https://www.youtube.com/watch?v=Cydzolb0eIs", 2)

    @staticmethod
    def confirm_quit():
        options = "Are you sure that you want to quit:(y/n)\n"
        result = raw_input(options)
        if result == 'y' or result == 'yes' or result == '1':
            sys.exit()
        else:
            return


    def get_url(self):
        self.api_url = raw_input("Please insert URL to API :")
        validator = Validator()
        if validator.validate_url(self.api_url):
            protocole = MainMenu.create_prompt(
                "Please choose your protocole",
                "REST", "SOAP"
            )

            if protocole == 1:
                rest = RestFuzzer()
                rest.start_fuzzing()

            elif protocole == 2:
                soap = SoapFuzzer()
                soap.start_fuzzing()
            else:
                print "Nice try..."
                print menu.delimiter_line
        else:
            MainMenu.error_message("Invalid URL !")
            return


if __name__ == '__main__':
    menu = MainMenu()

    print menu.welcome_message
    print menu.delimiter_line

    while 1:
        mode = MainMenu.create_prompt(
            "Please choose your action",
            "Fuzz API service", "Quit")

        if mode == '1':
            menu.get_url()

        elif mode == '2':
            MainMenu.confirm_quit()

        elif mode == 'sssr':
            MainMenu.play_me_something()

        else:
            print "Hey hey, let's focus here,shall we?"
            print menu.delimiter_line