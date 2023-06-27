import http.server
import subprocess

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        output = subprocess.check_output(['inxi', '-Fxz']).decode('utf-8')
        self.wfile.write(output.encode('utf-8'))

def main():
    server = http.server.HTTPServer(('localhost', 8000), RequestHandler)
    print('Server started on localhost:8000')
    server.serve_forever()

if __name__ == '__main__':
    main()
