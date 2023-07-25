from http.server import BaseHTTPRequestHandler, HTTPServer
from passw import gen_pass

class apiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/ping':
            # Handle the /ping endpoint as before
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = "ping-pong"
            self.wfile.write(message.encode())

        elif self.path == '/password':
            # Handle the /password endpoint
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Generate a random password using the gen_pass function from the passw package
            #password_length = 12  # You can set the desired password length here
            generated_password = gen_pass()
            message = "Generated password: {}".format(generated_password)

            self.wfile.write(message.encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 Not Found')

def run_server():
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, apiHandler)
    print('Starting server on http://{}:{}'.format(*server_address))
    httpd.serve_forever()

run_server()

