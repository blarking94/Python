import sys

# Just a variable
my_name = "Ben"

def fib(n=10):    
	""" write Fibonacci series up to n with 10 as the default value"""

	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b

	print()

def print_path():
	""" Searches for Python Modules in the following paths and orders.
	
	The directory containing the input script (or the current directory when no file is specified)
	If PYTHONPATH is defined in system environmnts then this location is also checked
	The installation-dependent default."""
	print(sys.path)

def print_doc():
	""" Prints out the doc string for this function.
	
	Hello, I'm some doc string that is about to be printed out
	by the print statement below! If I've not been compiled with the option -OO that is .."""
	print(print_doc.__doc__)


if __name__ == "__main__":
	""" Entry function for the module if run as script.

	Checks to see if a value for fib was passed in to pass onto the function.
	If not then the default value for fib will be used."""
	
	if len(sys.argv) > 1:
		fib(int(sys.argv[1]))
	else:
		fib()

	#print_path()
	print_doc()
    