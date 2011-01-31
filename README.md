=======
APyMongo
=======
**Info** A tornado-based asynchronous version of the pymongo driver for MongoDB.

**Author** Dan Yamins <dyamins@gmail.com>

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

1. install mongodb
2. pull the apymongo repo, and 
3. go to directory where you pulled the repo and do the usual "python setup.py install" command. 


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

For more see the **examples** section of the docs.  To use a given example:

0. Make sure you have installed mongo and apymongo (and tornado), and that 
a MongoDB instance is running on localhost:27017 (the default).

1. cd /path/to/apymongo/doc/examples

2. python [desired_example_file.py]

3. Open a web broweser and point it to localhost:8000



Documentation
=============

Currently, there is no separate documentation for this project. Essentially, 
APyMongo's API is identical to pymongo's except for the following:

- **callbacks**:  Every pymongo method that actually hits the database for a response
(i.e. sends a message to the mongo server and expects a return message) 
now has a *callback* argument, a single-argument executable to which Tornado will
pass the contents of the returned message when it is ready to be read. 

- Cursors have no *next* method.  Instead, to obtain the equivalent of ``list(cursor.find())",
use the **loop**.

- The Connection method has a *io_loop* argument, to which you can pass an existing 
tornado.io_loop object for the streams to attach to.


Testing
=======

The easiest way to run the tests is to install `nose
<http://somethingaboutorange.com/mrl/projects/nose/>`_ (**easy_install
nose**) and run **nosetests** or **python setup.py test** in the root
of the distribution. Tests are located in the *test/* directory.

Currently, the tests are very scant (and, something using the tornado.testing framework
is not working quite right ...)


Limitations
===========

APymongo currently does not handle:

- master-slave connections
- DBRefs. 
- the *explain* method
