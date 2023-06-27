import http.server
import socketserver

PORT = 8000

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # send a response header
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # write some HTML content
        self.wfile.write(b"<html><head><title>My Server</title></head>")
        self.wfile.write(b"<body><h1>Hello from my server!</h1>")
        # create a form for user input
        self.wfile.write(b"<form method='POST'>")
        self.wfile.write(b"Enter some words: <input type='text' name='words'>")
        self.wfile.write(b"<input type='submit' value='Submit'>")
        self.wfile.write(b"</form></body></html>")

    def do_POST(self):
        # get the length of the data sent by the client
        length = int(self.headers.get("Content-length", 0))
        # read the data from the request body
        data = self.rfile.read(length).decode()
        # parse the data as a query string
        words = data.split("=")[1]
        # send a response header
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        # write some text content
        self.wfile.write(b"You entered: ")
        self.wfile.write(words.encode())

Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
