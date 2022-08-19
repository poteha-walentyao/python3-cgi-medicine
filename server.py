from http.server import HTTPServer, CGIHTTPRequestHandler


server_adress = ("", 8080)
httpd = HTTPServer(server_adress, CGIHTTPRequestHandler)
httpd.serve_forever()

