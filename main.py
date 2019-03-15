#!/usr/bin/env python
# coding:utf-8
import json
from urlparse import urlparse, parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
from geoip import geolite2


class S(BaseHTTPRequestHandler):
        @staticmethod
        def startHTTPServer():
                os.system("python -m SimpleHTTPServer 8081 &")

        def __check(self, ip):
                match = geolite2.lookup(ip)
                if match is not None:
                        print match
                        if match.continent == 'EU':
                                return '<meta http-equiv="refresh" content="0; URL=http://localhost:8081/article13.html">'

                return ""

        def __setBinaryHeader(self):
                self.send_response(200)
                self.send_header("Content-Type", "application/octet-stream")
                self.end_headers()

        def __setHtmlHeader(self):
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()

        def do_GET(self):
                print "\x1b[1;30;37m[INFO] Incoming get request \x1b[0;0;0m"
                params = parse_qs(urlparse(self.path).query)
                if params is not None:
                        try:
                                res = self.__check(params['ip'][0])
                                self.__setHtmlHeader()
                                self.wfile.write(res)
                                return

                        except Exception, e:
                                print e

                self.__setHtmlHeader()
                self.wfile.write("")


        def do_HEAD(self):
                self.__setHtmlHeader()

        def do_POST(self):
                print "\x1b[1;30;37m[INFO] Incoming post request \x1b[0;0;0m"
                try:
                        length = int(self.headers['Content-Length'])
                        post_data = parse_qs(self.rfile.read(length).decode('utf-8'))
                        if post_data is not None:
                                print post_data
                                try:
                                        res = self.__check(post_data['ip'][0])
                                        self.__setHtmlHeader()
                                        self.wfile.write(res)
                                        return

                                except Exception, e:
                                        print e

                        self.__setHtmlHeader()
                        self.wfile.write("")

                except Exception, e:
                        print e


def run(server_class=HTTPServer, handler_class=S, port=8080):
        server_address = ('0.0.0.0', port)
        S.startHTTPServer()
        print 'Starting EU-Geoblocker on port', port, "..."
        httpd = server_class(server_address, handler_class)
        try:
                print "Serverstatus: \x1b[0;30;42m [ONLINE] \x1b[0;0;0m"
                httpd.serve_forever()
        except Exception, e:
                print e.message


if __name__ == "__main__":
        from sys import argv

        if len(argv) == 2:
                run(port=int(argv[1]))

        else:
                run()
