
# This file demonstrates syntax errors, exceptions, how to handle exceptions and 
# custom error handling classes 

import logging as log

#There's two problems here, a syntax error one and a type exception
for i in range(0,5):
	print("Amazing Numbers! " + str(i))

#Hold the program until user inputs a number 
while True:
    try:
        x = int(input("Please enter a number: "))
        #print(not_defined)
     # Handle the Value Error 
    except (ValueError, NameError):
     	#print("Oops!  That was no valid number.  Try again...")
     	# We can rename errors that we catch, e.g ve 
       print("Oops!  That was no valid number.  Try again...")
    finally:
    	print("we didn't make it")
    	break

#Python doesn't like dividing by 0
def this_fails():
    x = 1/0

#Catch the Zero Division Error
try:
    this_fails()
except ZeroDivisionError as err:
	print('Handling run-time error:', err)

#Don't catch it ...
this_fails()

#Force an Error 
raise NameError("Fatal Name Error ")




# User Defined Errors + Custom Log Handler! 

class myAppError(Exception):

    def __init__(self, value):
        """
        When the error is initialized we set the logger for the application and the errors error message.

        Parameters
            value (str) : The error message.
        """
        
        self.value = value

        # Create a logger 
        self.error_log = log.getLogger("error_log")
        # Stream everything to console at loggers set level
        formatter = log.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s ', datefmt='%m/%d/%Y %I:%M:%S')
        file_handler = log.FileHandler(filename = "errors.log", mode = 'a+')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(log.WARNING)
        self.error_log.addHandler(file_handler)
        self.do_something()
        
    def do_something(self):
        """
        Here we do whatever we want! Could escape to pager duty, write to an additional file or log. 
        """
        self.error_log.error("My App Error: " + str(self.value))  

# Catch any exception and throw custom error! 
try:
	print(something_not_defined)
except Exception:
    raise myAppError("Oh No!")  