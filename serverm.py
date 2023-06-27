import http.server
import os

# Define the output of the command to display
command_output = os.popen("inxi -Fxz").read()

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Set the response status and headers
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Write the output of the command
        self.wfile.write(bytes("<pre>{}</pre>".format(command_output), "utf-8"))

# Start the HTTP server
httpd = http.server.HTTPServer(('localhost', 8001), RequestHandler)
print("Server started on port 8001")
httpd.serve_forever()
