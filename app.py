from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import datetime, pytz 

serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>HOURS</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>NY: "+ str(datetime.datetime.now(pytz.timezone('US/Eastern'))) +"</p>" ,"utf-8"))
            self.wfile.write(bytes("<p>Berlin: "+ str(datetime.datetime.now(pytz.timezone('Europe/Berlin'))) +"</p>" ,"utf-8"))
            self.wfile.write(bytes("<p>Tokyo: "+ str(datetime.datetime.now(pytz.timezone('Asia/Tokyo'))) +"</p>" ,"utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(json.dumps({'response': '200'}), 'utf-8'))


if __name__ == "__main__":        
    webServer = HTTPServer(('', serverPort), MyServer)
    print("Server started in %s" % (serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
