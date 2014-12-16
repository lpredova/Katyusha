__author__ = 'lovro'
import sys
import webbrowser


class Helper:


    def __init__(self):
        pass

    @staticmethod
    def welcome_message():
        logo = "  _   __      _                   _           \n" \
               " | | / /     | |                 | |          \n" \
               " | |/ /  __ _| |_ _   _ _   _ ___| |__   __ _ \n" \
               " |    \ / _` | __| | | | | | / __|  _ \ / _` |\n" \
               " | |\  \ (_| | |_| |_| | |_| \__ \ | | | (_| |\n" \
               " \_| \_/\__,_|\__|\__, |\__,_|___/_| |_|\__,_|\n" \
               "                   __/ |                      \n" \
               "                  |___/                       \n" \
               "REST and SOAP fuzzer                          \n"
        print logo

    @staticmethod
    def delimiter_line():
        print "################################################"


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
        Helper.delimiter_line()

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