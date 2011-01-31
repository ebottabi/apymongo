import json

import tornado.web

import apymongo 
from apymongo import json_util

import base


class TestHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):     
     
        self.writing = False    
        self.write('[')
        
        conn = apymongo.Connection()
        coll = conn['testdb']['__ASYNCTEST__']
        cursor = coll.find(callback=self.handle,processor = self.process).limit(1000)       
        cursor.loop()
        

    def handle(self,response):
        self.write(']')
        self.finish()
               
               
    def process(self,r,collection):
    
		self.write((',' if self.writing else '') + json.dumps(r,default=json_util.default))
		self.flush()
		if not self.writing:
			self.writing = True
			
	    

if __name__ == "__main__":
    base.main(TestHandler)

  
  
          
        
