from http.server import BaseHTTPRequestHandler, HTTPServer
#These classes are necessary to handle HTTP requests and create an HTTP server.
class apiHandler(BaseHTTPRequestHandler):
    #we will override its methods to define how the API responds to different types of HTTP requests.
    def do_GET(self):
        # do_GET method is called when the server receives a GET request.


        if self.path == '/ping':
            #it checks if the path of the incoming request is /ping.
            # Send response status code
            self.send_response(200)

            # Send headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Send response content
            message = "ping-pong"
            self.wfile.write(message.encode())
            # sends the response content back to the client
        else:
            #  return 404 Not Found
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'go to ping page')

def run_server():
    # Set the server address and port
    server_address = ('localhost', 8080)

    # Create an HTTP server with the custom request handler
    httpd = HTTPServer(server_address, apiHandler)
    print('Starting server on http://{}:{}'.format(*server_address))

    # Start the server to handle incoming requests
    httpd.serve_forever()


run_server()

