from http.server import BaseHTTPRequestHandler
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        res = requests.get(
            "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN")
        res = res.json()
        imageUrl = "https://cn.bing.com"+res["images"][0]["url"]
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.wfile.write(imageUrl.encode())
        return