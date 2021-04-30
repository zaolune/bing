from http.server import BaseHTTPRequestHandler
import requests


class handler(BaseHTTPRequestHandler):
    def set_header(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/x-javascript')
        self.end_headers()
        return

    def get_oneWord(self):
        res = requests.get("https://v1.hitokoto.cn")
        return res.json()['hitokoto']

    def build_javaScript(self, res):
        javascript = """
        document.getElementById("voneword").innerHTML='%s'
        """ % (res)
        return javascript.encode('utf-8')

    def do_GET(self):
        self.set_header()
        res = self.get_oneWord()
        js = self.build_javaScript(res)
        self.wfile.write(js)
        return
