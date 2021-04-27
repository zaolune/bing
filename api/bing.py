from http.server import BaseHTTPRequestHandler
import requests
import time
import json
import os
from os.path import join


class handler(BaseHTTPRequestHandler):
    def set_Header(self, imageUrl):
        self.send_response(302)
        self.send_header('Location', imageUrl)
        self.end_headers()
        return

    def get_Current_FilesName(self):
        recordName = time.strftime("%Y-%m-%d", time.localtime())+'.txt'
        return recordName

    def set_Record(self, json):
        recordName = self.get_Current_FilesName()
        with open(join('data', recordName), 'w') as files:
            files.write(json)
        print(recordName+"saved successfully!")
        files.close()
        return

    def get_Current_Record(self):
        recordName = self.get_Current_FilesName()
        with open(join('data', recordName), 'w') as files:
            data = files.read()
        print("get today's record successfully!")
        return json.dumps(data)

    def is_saved(self):
        recordName = self.get_Current_FilesName()
        return os.path.exists(join('data', recordName))

    def do_GET(self):
        if not self.is_saved():
            res = requests.get(
                "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN")
            res = res.json()
            self.set_Record(res)
            imageUrl = "https://cn.bing.com"+res["images"][0]["url"]
            print(imageUrl)
            return self.set_Header(imageUrl)
        else:
            res = self.get_Current_Record()
            imageUrl = "https://cn.bing.com"+res["images"][0]["url"]
            print(imageUrl)
            return self.set_Header(imageUrl)

