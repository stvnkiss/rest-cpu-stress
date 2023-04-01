from stressinjector.cpu import CPUStress
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        seconds = int(query_components["seconds"])
        CPUStress(seconds=seconds).run()
        self.wfile.write(b'Stress done\n')

def main():
    host = '0.0.0.0'
    port = 8000
    server = HTTPServer((host, port), RequestHandler)
    print('Server listening on port', port)
    server.serve_forever()

if __name__ == '__main__':
    main()
