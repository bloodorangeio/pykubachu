#!/usr/bin/env python3

import os
from wsgiref.simple_server import make_server
import falcon

DIRNAME = os.path.dirname(os.path.realpath(__file__))
PIKA_COLOR = os.environ.get('PIKA_COLOR', '#00a3ff')

class PyKubachuHome:
    def on_get(self, req, resp):
        resp.content_type = 'text/html; charset=utf-8'
        body = '<html><head><title>PyKubachu</title></head>'
        body += '<body style="background:'+PIKA_COLOR+';margin: 0px;">'
        body += '<img src="/images/pykubachu.png"/>'
        body += '</body></html>'
        resp.body = body

class PyKubachuImage(object):
    def on_get(self, req, resp, filename):
        resp.content_type = 'image/png'
        image_path = DIRNAME+'/images/'+filename
        resp.stream = open(image_path, 'rb')
        resp.stream_len = os.path.getsize(image_path)

app = falcon.API()
app.add_route('/', PyKubachuHome())
app.add_route('/images/{filename}', PyKubachuImage())

if __name__ == '__main__':
    with make_server('', 8080, app) as httpd:
        print('Serving on port 8080...')
        httpd.serve_forever()
