__author__ = 'lovro'

import SimpleHTTPServer
import SocketServer
import socket



class Server(object):

    _PORT = 8080
    _instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Server, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def check_for_service(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex(('127.0.0.1', self._PORT))

        if result == 0:
            return False
        else:
            s.close()
            return True

    def serve(self):

        if self.check_for_service():
            print "running localhost server..."
            handler = SimpleHTTPServer.SimpleHTTPRequestHandler
            httpd = SocketServer.TCPServer(("", self._PORT), handler)
            print "I'm listening....on 8080"
            httpd.serve_forever()
        else:
            return 0