import json

import tornado.web

import apymongo 
from apymongo import json_util

import base


class TestHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):     
        conn = apymongo.Connection()
        coll = conn['testdb']['__ASYNCTEST2__']
        cursor = coll.find(callback=self.handle)
        cursor.loop()
        

    def handle(self,response):
        self.write(json.dumps(response,default=json_util.default))
        self.finish()
              

if __name__ == "__main__":
    base.main(TestHandler)

  
  
          
     