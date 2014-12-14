__author__ = 'lovro'

import urllib2
import httplib


class Validator:
    def __init__(self):
        pass


    def __validate_url(self, url):
        try:
            urllib2.urlopen(url)
            return True  # URL Exist

        except ValueError, ex:
            return False  # URL not well formatted

        except urllib2.URLError, ex:
            return False  # URL don't seem to be alive


    def validate_url(self, url):

        if self.__validate_url(url):
            return True
        else:
            return False