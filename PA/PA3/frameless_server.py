import http.server
import socketserver


class Handler(http.server.SimpleHTTPRequestHandler):
    # def do_GET(self):
    #     self.send_response(200)
    #     self.send_header("Content-type", "text/html")
    #     self.end_headers()
    #     self.wfile.write(b"<html><body><h1>Hello, World!</h1></body></html>")
    pass


with socketserver.TCPServer(("", 8000), Handler) as httpd:
    print("Server started at http://localhost:8000")
    httpd.serve_forever()
