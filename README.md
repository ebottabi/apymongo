=======
APyMongo
=======
:Info: A tornado-based asynchronous version of the pymongo driver for MongoDB.
:Author: Dan Yamins <dyamins@gmail.com>

About
=====

APyMongo is an asynchronous version of [the PyMongo driver for MongoDB](http://api.mongodb.org/python).
APyMongo uses the [tornado iostream eventloop](github.com/facebook/tornado/blob/master/tornado/iostream.py) 
to drive asychronous requests.  A primary use of APyMongo is to serve MongoDB-backed websites in an efficient asynchronous manner
via the [tornado web server](www.tornadoweb.org), but it can be used wherever one wants to drive multiple efficient 
highthrouput read-write connections to a MongoDB instance.   


Installation
============

For now, the project is just a github repo ([https://github.com/yamins81/apymongo]).  
The install process is: 

1) install mongodb
2) pull the apymongo repo, and 
3) go to directory where you pulled the repo and do the usual "python setup.py install" command. 


Dependencies
============

Mongo:  APyMongo works for the same MongoDB distributions that PyMongo works on. 

Python:  APyMongo requires Python >=2.4.    

Tornado:  IMPORTANT!!! You MUST must be using the a recent pull from the Tornado repository to  
run APyMongo.   APyMongo depends on a recent addition to the tornado.iostream module that is NOT
present in the current release. 

Additional dependencies are:

- (to generate documentation) [sphinx](http://sphinx.pocoo.org/)
- (to auto-discover tests) [nose](http://somethingaboutorange.com/mrl/projects/nose/).


Examples
========
Here's a basic example that can be used in a Tornado web server:

	import json
	import tornado.web
	
	import apymongo 
	from apymongo import json_util
		
	class TestHandler(tornado.web.RequestHandler):
	
		@tornado.web.asynchronous
		def get(self):     
			connection = apymongo.Connection()		
			collection = conn['testdb']['testcollection']
			coll.find_one(callback=self.handle)
			
		def handle(self,response):
			self.write(json.dumps(response,default=json_util.default))
			self.finish()

For more see the *examples* section of the docs


Documentation
=============

You will need sphinx_ installed to generate the
documentation. Documentation can be generated by running **python
setup.py doc**. Generated documentation can be found in the
*doc/build/html/* directory.


Testing
=======

The easiest way to run the tests is to install `nose
<http://somethingaboutorange.com/mrl/projects/nose/>`_ (**easy_install
nose**) and run **nosetests** or **python setup.py test** in the root
of the distribution. Tests are located in the *test/* directory.

.. _sphinx: http://sphinx.pocoo.org/


Limitations
===========

APymongo currently does not handle

- master-slave connections
- DBRefs. 
