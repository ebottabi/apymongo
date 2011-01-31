import json

import tornado.web

import apymongo 
from apymongo import json_util

import base

class TestHandler(tornado.web.RequestHandler):

    
    @tornado.web.asynchronous
    def get(self):     
    
        self.connection = apymongo.Connection()
        
        coll = self.connection['testdb']['__ASYNCTEST3__']
        to_insert = {"testkey1":22,
                     "testkey2":[2,3], 
                     "testkey3":{"inner1":2,
                                 "inner2":'testval'}}

        coll.insert(to_insert,callback=self.count_handler)
        
    def count_handler(self,response):
        
        def callback(r):
            self.final_handler(response,r)
        
        coll = self.connection['testdb']['__ASYNCTEST3__']
        
        coll.count(callback = callback)


    def final_handler(self,rec_id, response):
        
        msg = "You just inserted record " + str(rec_id) + '.  There are now ' + str(response) + ' records.'
              
        self.write(msg)
        self.finish()

if __name__ == "__main__":
    base.main(TestHandler)
  
  
          
    