from http.server import BaseHTTPRequestHandler
import requests
import shutil

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        res = requests.get(
            "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN")
        res = res.json()
        imageUrl = "https://cn.bing.com"+res["images"][0]["url"]
        print(imageUrl)
        # template = """
        #     <!DOCTYPE html>
        #     <html lang="zh-hans">
        # <head>
        #     <meta charset="UTF-8">
        #     <meta http-equiv="X-UA-Compatible" content="IE=edge">
        #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
        #     <title>Document</title>
        # </head>
        #     <body>
        #     <img src="%s" alt="">
        #     </body>
        #     </html>
        # """ % (imageUrl)
        self.send_response(200)
        self.send_header('Content-type', 'image/jpeg')
        self.end_headers()
        with open(imageUrl,'rb') as images:
            shutil.copyfileobj(images, self.wfile)
        return
