__author__ = 'Milan'

class PayloadReader:

    _filePath = 'data/MySQL.fuzz.txt'

    def __init__(self):
        pass

    def setFilePath(self, path):
        self._filePath = path

    def getFilePath(self):
        return self._filePath

    def getFuzzStrings(self):
        fuzzFile = open(self._filePath, "r")
        fuzzVectors = []

        for line in fuzzFile:
            if(line.startswith('#') != 'true'):
                fuzzVectors.append(line.strip())

        fuzzFile.close()
        return fuzzVectors


reader = PayloadReader()

strings = reader.getFuzzStrings()

print strings
