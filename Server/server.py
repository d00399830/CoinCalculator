from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import requests
import json
from socketserver import ThreadingMixIn
import random
from pycoingecko import CoinGeckoAPI

class MyRequestHandler(BaseHTTPRequestHandler):

    cg = CoinGeckoAPI()

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", self.headers["Origin"])
        self.send_header("Access-Control-Allow-Credentials", "true")
        BaseHTTPRequestHandler.end_headers(self) #calls the original end_headers

    def handleNotFound(self):
        self.send_response(404)
        self.send_header("Content-Type","text/plain")
        self.end_headers()
        self.wfile.write(bytes("The only reason you got this page was because you messed up, whoops", "utf-8"))

    def handleConvertCoin(self, usd, coin):
        cg = CoinGeckoAPI()
        getConvert = cg.get_price(ids=coin, vs_currencies='usd')
        priceConvert = int(usd)/getConvert[coin]['usd']
        priceConvert = "{:.10f}".format(priceConvert)
        data = {"coin": coin, "numOfCoins": priceConvert}
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(data), "utf-8"))   

    def do_GET(self):
        xSplit = self.path.split('/')
        print(xSplit)
        if xSplit[1] == "convert":
            self.handleConvertCoin(xSplit[2], xSplit[3])
        else:
            self.handleNotFound()

    def do_POSt(self): 
            self.handleNotFound()

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def main():
    #The main function <(*.*<) (^*.*^) (>*.*)>
    print("Beep Boop: Server Initialized - Please build additional Pylons")
    listen = ("127.0.0.1", 8080)
    server = ThreadedHTTPServer(listen, MyRequestHandler)
    server.serve_forever()  
    
main()
