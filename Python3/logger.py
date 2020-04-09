import logging as log

#As warning is the default level Nice Day won't be printed 
log.info("Nice Day!")
log.warning("Rain Ahead!")

#Writes to file at debug level 
log.basicConfig(filename='example.log', filemode='w', level=log.DEBUG)
log.debug('This message should go to the log file')
log.info('So should this')
log.warning('And this, too')

#Add formatting to the date and time 
log.basicConfig(filename='../example.log', filemode='w', level=log.DEBUG, 
	format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
log.debug('This message should go to the log file with a nice format')
log.info('So should this')
log.warning('And this, too')


# We can define different loggers! The root one and a fancy one
simple_log = log.getLogger(__name__)
simple_log.warning("simple log")

# Create a format object and a handler
formatter = log.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s  - %(funcName)s - %(message)s ' , datefmt='%m/%d/%Y %I:%M:%S')
file_handler = log.FileHandler(filename = "example.log", mode = 'w')
file_handler.setFormatter(formatter)
# Only Write warnings to the file
file_handler.setLevel(log.WARNING)

# Stream everything to console at loggers set level
console_handler = log.StreamHandler()

# Create a logger to use the handler and formatter 
fancy_log = log.getLogger("fancy_log")
fancy_log.addHandler(console_handler)
fancy_log.addHandler(file_handler)
fancy_log.setLevel(log.DEBUG)

fancy_log.debug("debug this!")
fancy_log.info("fancy_log")
fancy_log.warning("fancy_log warning message!")

def my_function():
	fancy_log.warning("This function was called!")

my_function()

# We can create custom handlers that extend existing ones to overwrite methods
class customStreamHandler(log.StreamHandler):

	# When emit is called, give a custom message
	def emit(self, msg):
		print("CUSTOM BIG ERROR MESSAGE")
		

# Create the super handler! a custom one...
superHandler = customStreamHandler()
superHandler.setLevel(log.ERROR)

fancy_log.addHandler(superHandler)
fancy_log.warning("don't worry")
fancy_log.error("ops")
