__author__ = 'Milan'
import os


class PayloadReader():
    filePath = "/lib/data/MySQL.fuzz.txt"

    def __init__(self):
        pass

    def set_file_path(self, path):
        self.filePath = path

    def get_file_path(self):
        return self.filePath

    def get_current_file_path(self):
        return os.path.abspath(os.curdir)

    def get_fuzz_strings(self):
        fuzz_file = open(self.get_current_file_path()
                         + self.filePath, "r")
        fuzz_vectors = []

        for line in fuzz_file:
            if line.startswith('#') != 'true':
                fuzz_vectors.append(line.strip())

        fuzz_file.close()
        return fuzz_vectors