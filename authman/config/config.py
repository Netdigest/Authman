from os import environ

class Config:
	ENV = environ.config("FANTOM_AUTHMAN_ENV","PRODUCTION")
	TESTING = int(environ.config("FANTOM_AUTHMAN_TESTING","0")) 
	DEBUG = int(environ.config("FANTOM_AUTHMAN_DEBUG","0"))
