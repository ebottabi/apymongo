import os
import json
import functools

import tornado.web
import tornado.httpclient
import apymongo as apm

from apymongo import json_util


class TestHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        
        io_loop = self.settings['io_loop']
        conn = apm.Connection(io_loop = io_loop)
  
        db = conn['testdb']
        
        coll = db['__ASYNCTEST2__']
        
        callback = self.handle
        
        cursor = coll.find(spec={"a":{"$lt":200}},callback=callback).limit(1000)
        cursor.loop()
        
        #coll.insert({"a":1},callback=callback)
          
          
    def handle(self,response):

        self.write(json.dumps(response,default=json_util.default))
        
        self.finish()
       
  
  
  
          
        
