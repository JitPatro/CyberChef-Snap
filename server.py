import http.server
import socketserver
import socket
from contextlib import suppress

PORT = 9090
DIRECTORY = "/snap/cyberchef/current"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
open = sock.connect_ex(('localhost', PORT))

class SilentServer(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        pass


if open == 0:
    pass
else:
    with suppress(BrokenPipeError, KeyboardInterrupt):
        with socketserver.TCPServer(("localhost", PORT), SilentServer) as httpd:
            httpd.serve_forever()


