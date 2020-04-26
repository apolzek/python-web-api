import json
from http.server import HTTPServer, BaseHTTPRequestHandler

# python -m http.server
# uvidorn = The lightning-fast ASGI server
dados = {"canal": "LinuxTips", "msg": "VAIII"}  # dict


class API(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # ok
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(dados).encode("utf-8"))


server = HTTPServer(("0.0.0.0", 8080), API)
server.serve_forever()
